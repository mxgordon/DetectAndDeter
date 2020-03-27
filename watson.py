import speech_recognition as sr


URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/24dbf68e-4a5d-4455-b82c-b86e1c0c449d"
API_KEY = "zPJij17cD8uAVUsaWqRgZPyGt9CH5q8XuwNGurfFhtXW"

USERNAME = "55517463-5e48-47f6-9a19-f0001ef9349a"
USERNAME2 = "24dbf68e-4a5d-4455-b82c-b86e1c0c449d"

sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

device_id = 0

with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    
    r.recognize_ibm(source, USERNAME, API_KEY)


"""
curl -k -X POST \
  --header "Content-Type: application/x-www-form-qurlencoded" \
  --header "Accept: application/json" \
  --data-urlencode "grant_type=urn:ibm:params:oauth:grant-type:apikey" \
  --data-urlencode "apikey=<zPJij17cD8uAVUsaWqRgZPyGt9CH5q8XuwNGurfFhtXW>" \
  "https://iam.cloud.ibm.com/identity/token"
  
  
  
    curl -u 55517463-5e48-47f6-9a19-f0001ef9349a:zPJij17cD8uAVUsaWqRgZPyGt9CH5q8XuwNGurfFhtXW \
   "https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/speech-to-text/api"
"""