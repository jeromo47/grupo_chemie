
import csv
import subprocess
from pathlib import Path
from dataclasses import dataclass, asdict

ROOT = Path('/home/jero/cloud/02_proyectos/grupo_familiar/00_fuente_drive')
OUT_BASE = Path('/home/jero/cloud/02_proyectos/grupo_familiar/13_conocimiento_generado/pipeline_extraccion_documental')
TEXT_DIR = OUT_BASE / 'textos'
OCR_DIR = OUT_BASE / 'ocr_pdf'
REPORT_CSV = OUT_BASE / 'reporte_extraccion.csv'

TEXT_DIR.mkdir(parents=True, exist_ok=True)
OCR_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class Row:
    ruta_relativa: str
    tipo_archivo: str
    metodo: str
    texto_len: int
    salida_texto: str
    salida_pdf_ocr: str
    estado: str
    notas: str


def run(cmd, timeout=300):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)


def safe_slug(rel_path: str) -> str:
    s = rel_path.replace('/', '__').replace(' ', '_')
    bad = '<>:"\\|?*'
    for ch in bad:
        s = s.replace(ch, '_')
    return s


def extract_pdf(pdf: Path, rel: str) -> Row:
    slug = safe_slug(rel)
    txt_out = TEXT_DIR / f'{slug}.txt'
    ocr_pdf_out = OCR_DIR / f'{slug}.ocr.pdf'

    direct = run(['pdftotext', str(pdf), '-'])
    direct_text = direct.stdout if direct.returncode == 0 else ''
    direct_len = len(direct_text.strip())

    if direct_len > 80:
        txt_out.write_text(direct_text, encoding='utf-8')
        return Row(rel, 'pdf', 'pdftotext', direct_len, str(txt_out.relative_to(OUT_BASE)), '', 'OK', '')

    ocr = run(['ocrmypdf', '-l', 'spa', '--skip-text', str(pdf), str(ocr_pdf_out)], timeout=1200)
    if ocr.returncode != 0 or not ocr_pdf_out.exists():
        return Row(rel, 'pdf', 'ocrmypdf', 0, '', '', 'ERROR', (ocr.stdout or '')[:500])

    post = run(['pdftotext', str(ocr_pdf_out), '-'])
    post_text = post.stdout if post.returncode == 0 else ''
    post_len = len(post_text.strip())
    if post_len > 0:
        txt_out.write_text(post_text, encoding='utf-8')
        return Row(rel, 'pdf', 'ocrmypdf+pdftotext', post_len, str(txt_out.relative_to(OUT_BASE)), str(ocr_pdf_out.relative_to(OUT_BASE)), 'OK', '')

    return Row(rel, 'pdf', 'ocrmypdf+pdftotext', 0, '', str(ocr_pdf_out.relative_to(OUT_BASE)), 'VACIO', 'OCR sin texto útil')


def main():
    targets = [
        ROOT / 'DOCUMENTACION/DOCUMENTACION CHEMIE/ESCRITURA PDF',
    ]
    pdfs = []
    for t in targets:
        pdfs.extend(sorted(t.rglob('*.pdf')))
    rows = []
    for pdf in pdfs:
        rel = str(pdf.relative_to(ROOT))
        print('PROCESANDO', rel, flush=True)
        try:
            rows.append(extract_pdf(pdf, rel))
        except Exception as e:
            rows.append(Row(rel, 'pdf', 'exception', 0, '', '', 'ERROR', str(e)[:500]))
    with REPORT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()) if rows else list(Row('', '', '', 0, '', '', '', '').__dict__.keys()))
        w.writeheader()
        for r in rows:
            w.writerow(asdict(r))
    print('REPORT', REPORT_CSV)
    print('TOTAL', len(rows))
    ok = sum(1 for r in rows if r.estado == 'OK')
    vacio = sum(1 for r in rows if r.estado == 'VACIO')
    err = sum(1 for r in rows if r.estado == 'ERROR')
    print('OK', ok, 'VACIO', vacio, 'ERROR', err)

if __name__ == '__main__':
    main()
