import requests
import sys
import re
import webbrowser

def replace_between(text_before, first, last):
  match = re.search(r'{}(.*){}'.format(first, last), text_before, re.S)
  groups = match.group()
  value = ""
  for group in groups:
    value += group
  return text_before.replace(value, "")

def add_css_file(text_before, css_path):
  to_replace = '<head>'
  new_css = '<head><link rel="stylesheet" href="{}" />'.format(css_path)
  return text_before.replace(to_replace, new_css)

def remove_message_container(text):
  to_search = '<div id="sp_message_container_484120" style="display: block;">'
  to_replace = '<div id="sp_message_container_484120" style="display: none;">'
  return text.replace(to_search, to_replace)

def main():
  # Get URL from sys
  url = sys.argv[1]

  # Request page.
  page = requests.get(url).text

  # Add static css styles.
  style_1 = './main.css'
  style_2 = './article.css'
  page = add_css_file(page, style_1)
  page = add_css_file(page, style_2)

  # Remove cookie popup.
  start_tag = '<template id="article-no-consent-notification">'
  end_tag = 'template>'
  page = replace_between(page, start_tag, end_tag)

  # Write page
  with open('index.html', "w") as file:
      file.write(page)

  # Open webbrowser
  chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
  webbrowser.get(chrome_path).open('index.html')

if __name__ == "__main__":
    main()



