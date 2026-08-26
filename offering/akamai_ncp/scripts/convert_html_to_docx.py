import os
import glob
from bs4 import BeautifulSoup
from docx import Document
from htmldocx import HtmlToDocx

def convert_html_to_docx(html_path, docx_path):
    print(f"변환 시작: {html_path} -> {docx_path}")
    document = Document()
    new_parser = HtmlToDocx()
    
    # HTML 파일 읽기
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # BeautifulSoup으로 본문 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # report-card 클래스 내부의 컨텐츠가 메인 본문
    body_content = soup.find('div', class_='report-card')
    if not body_content:
        body_content = soup.find('body')
    
    html_str = str(body_content) if body_content else html_content
    
    # docx 문서에 HTML 추가
    new_parser.add_html_to_document(html_str, document)
    
    # 문서 저장
    document.save(docx_path)
    print(f"변환 완료: {docx_path}")

def main():
    # 스크립트 파일 기준으로 docs 폴더의 절대 경로 찾기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.abspath(os.path.join(current_dir, '..', 'docs'))
    
    # docs 폴더 내부의 모든 html 파일 탐색
    html_files = glob.glob(os.path.join(docs_dir, '**', '*.html'), recursive=True)
    
    if not html_files:
        print("docs 폴더 내에서 HTML 파일을 찾을 수 없습니다.")
        return
        
    for html_file in html_files:
        docx_file = os.path.splitext(html_file)[0] + '.docx'
        try:
            convert_html_to_docx(html_file, docx_file)
        except Exception as e:
            print(f"{html_file} 변환 중 오류 발생: {e}")

if __name__ == '__main__':
    main()
