import urllib.request
import urllib.parse
import json

# We will just print the instructions to run the test because handling multipart form data with urllib is verbose
# and installing requests might not have happened.
# Actually, let's write a simple test script that assumes 'requests' is available OR use pure python.
# Since we installed 'requirements.txt' and we didn't add 'requests', we might not have it.
# But 'requirements.txt' has 'Flask', 'pdfplumber', 'python-docx', 'scikit-learn', 'nltk'.
# None of these guarantee 'requests'.

# Let's try to import requests, if fails, we skip.
try:
    import requests
except ImportError:
    print("Requests library not found. Please install it to run this test script, or manually test in browser.")
    exit(1)

def test_app():
    url = 'http://127.0.0.1:5000/result'
    files = {'resume': open('test_resume.docx', 'rb')}
    data = {'job_description': 'Looking for a Python Developer with experience in Flask, SQL, and Docker. Must know Git.'}
    
    try:
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("SUCCESS: Endpoint returned 200 OK")
            if "Analysis Result" in response.text:
                print("SUCCESS: Response contains 'Analysis Result'")
            else:
                print("FAILURE: Response does not contain expected text")
        else:
            print(f"FAILURE: Endpoint returned {response.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_app()
