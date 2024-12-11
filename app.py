from flask import Flask, render_template, request, jsonify
import dns.resolver
import requests
from urllib.parse import urlparse
import re

app = Flask(__name__)

def validate_svg_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and 'image/svg+xml' in response.headers.get('content-type', ''):
            return True, response.text
    except:
        pass
    return False, None

def check_bimi_record(domain):
    try:
        # Look up BIMI record
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(f'default._bimi.{domain}', 'TXT')
        
        bimi_data = {}
        for rdata in answers:
            txt_string = rdata.strings[0].decode('utf-8')
            if 'v=BIMI1' in txt_string:
                # Extract logo URL
                match = re.search(r'l=([^;]+)', txt_string)
                if match:
                    logo_url = match.group(1)
                    is_valid_svg, svg_content = validate_svg_url(logo_url)
                    
                    bimi_data = {
                        'has_record': True,
                        'record': txt_string,
                        'logo_url': logo_url,
                        'is_valid_svg': is_valid_svg,
                        'svg_content': svg_content if is_valid_svg else None
                    }
                    return bimi_data
                
        return {'has_record': False}
    except:
        return {'has_record': False}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    domains = request.form.get('domains', '').split('\n')
    results = {}
    
    for domain in domains:
        domain = domain.strip()
        if domain:
            results[domain] = check_bimi_record(domain)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
