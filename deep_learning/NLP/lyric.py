#!/usr/bin/env python3

from bs4 import BeautifulSoup, NavigableString

import os
import sys

def extract_between_anchors(xhtml_content):
    '''a parser that extract content of poem
    created by deepseek

    input: xhtml file
    output:list contain dict
    '''
    soup = BeautifulSoup(xhtml_content, 'html.parser')
    results = []
    
    # Find all anchor tags with IDs
    anchors = soup.find_all('a', id=True)
    
    for i in range(len(anchors) - 1):
        start_anchor = anchors[i]
        end_anchor = anchors[i + 1]
        
        # Collect all nodes between start and end anchors
        content = []
        current = start_anchor.parent.next_sibling if start_anchor.parent else start_anchor.next_sibling
        
        while current and current != end_anchor.parent:
            if isinstance(current, NavigableString):
                if str(current).strip():
                    content.append(str(current))
            else:
                content.append(str(current))
            current = current.next_sibling
        
        results.append({
            'start_id': start_anchor['id'],
            'end_id': end_anchor['id'],
            'start_title': start_anchor.get_text(),
            'content': '\n'.join(content)
        })
    
    return results

def clean_up(raw_text):
    '''
    clean up text and remove a "<p></p>" and "\u200c"

    input: list contain dict from extract_between_anchors()
    output: poem text
    '''
    process = []
    
    for i in raw_text:
        process.append(i['content']) # getting poem text
    
    process = '~'.join(process) #change list to str ~ is end of each poem
    process = process.replace('\u200c', ' ') # remove nim-fasele
    
    # remove </p> and <p>
    process = process.replace('</p>\n<p>',' # ')  # end of mesra' sign
    process = process.replace('</p>','@')  # end of poem sign
    process = process.replace('<p>','') # beginning of poem
    return process
    

if __name__ == "__main__":
    args = sys.argv
    path = args[1]+'/'
    full_book = []
    file_ = os.listdir(path=path)
    for file in file_:
        if ('sec' in file) and (file.endswith('xhtml')) :
            with open(path+file, 'r', encoding='utf-8') as f :
                xhtml_content = f.read()
            
            this_section = extract_between_anchors(xhtml_content)
            full_book.extend(this_section)
            final = clean_up(full_book)
    with open('manocheri_lyric.txt', 'w' ) as f:
        f.write(final)
