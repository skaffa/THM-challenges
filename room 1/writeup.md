# Web Challenge: Hidden Headers

## Challenge Description
A login system with a hidden authentication mechanism. Can you find the admin credentials?

## Solution

### Step 1: Initial Analysis
The challenge presents a simple login form with three fields:
- Username
- Password
- 2FA Code

The form is styled with basic CSS and appears to be a standard login interface.

### Step 2: Cookie Investigation
Using browser developer tools (F12), inspect the cookies:
- A cookie named `tfat` is automatically set
- Value: `324641544F4B454E3A343134323632`
- This appears to be hex-encoded data

Decoding the hex:
```bash
echo "324641544F4B454E3A343134323632" | xxd -r -p
```
Output: `FLAG:414263`

### Step 3: Password Page Analysis
Visiting `/forgot-password` returns a 403 Forbidden response
- The error message appears to be a dead end
- However, checking the response headers reveals:
  - `X-PW-Hint: QXJzbWFkNjg=`
- This is base64 encoded
- Decoding it:
```bash
echo "QXJzbWFkNjg=" | base64 -d
```
Output: `ArsMad68`

### Step 4: Authentication
Using the discovered credentials:
- Username: `admin`
- Password: `Arsmad68`
- 2FA: `414263`

Submit these values to successfully authenticate and retrieve the flag.

## Key Concepts
- HTTP cookie manipulation
- Response header analysis
- Base64 and hex encoding/decoding
- Looking beyond obvious error messages
- Browser developer tools usage

## Tools Used
- Browser Developer Tools (F12)
- Base64 decoder
- Hex decoder
- Network tab for header inspection
