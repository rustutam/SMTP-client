from dataclasses import dataclass


@dataclass
class Header:
    name_from: str
    name_to: str
    subject: str
    names_to_copy: str
    date: str


@dataclass
class File:
    name_file: str
    file_type: str
    data: str

content_types = {
    '.txt': 'text/plain',
    '.pdf': 'application/pdf',
    '.mp3': 'audio/mpeg',
    '.html': 'text/html',
    '.json': 'application/json',
    '.xml': 'application/xml',
    '.jpg': 'image/jpeg',
    '.png': 'image/png',
    '.mp4': 'video/mp4'
}

