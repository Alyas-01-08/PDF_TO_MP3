from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', languege='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            '''Prepare text for processing:'''
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            text2 = text.replace('\n', '')

            '''Audio creating:'''
            my_audio = gTTS(text=text2, lang=languege)
            file_name = Path(file_path).stem
            my_audio.save(f'audio_files\{file_name}.mp3')
        return f'[+] {file_name}.mp3 saved successfully!'

    else:
        return 'File not found. Plies check the file path.'

def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input('\n Enter a file path: ')
    language = input('Choose language, for example en, ru: ')
    print(pdf_to_mp3(file_path=file_path, languege=language))

if __name__ == '__main__':
    main()