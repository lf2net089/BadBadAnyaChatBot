import json
import boto3
    
# Bedrock client used to interact with APIs around models
bedrock = boto3.client(
    service_name='bedrock', 
    region_name='us-east-2'
)
    
# Bedrock Runtime client used to invoke and question the models
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-2'
)
    

def handler(event, context):
     # System prompt that provides context or guidance to the model
     system_prompt = """ secret prompt """

     # Just shows an example of how to retrieve information about available models
     foundation_models = bedrock.list_foundation_models()
     matching_model = next((model for model in foundation_models["modelSummaries"] if model.get("modelName") == "Claude 3 Sonnet"), None)
    
     prompt = json.loads(event.get("body")).get("input").get("question")
     combined_prompt = f"{system_prompt} {user_input}"
    
     # The payload to be provided to Bedrock 
     body = json.dumps(
       {
          "prompt": prompt, 
          "maxTokens": 200,
          "temperature": 0.7,
          "topP": 1,
       }
     )
     
     # The actual call to retrieve an answer from the model
     response = bedrock_runtime.invoke_model(
       body=body, 
       modelId=matching_model["modelId"], 
       accept='application/json', 
       contentType='application/json'
     )
    
     response_body = json.loads(response.get('body').read())
    
     # The response from the model now mapped to the answer
     answer = response_body.get('completions')[0].get('data').get('text')
     
     return {
       'statusCode': 200,
       'headers': {
         'Access-Control-Allow-Headers': '*',
         'Access-Control-Allow-Origin': '*',
         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
       },
         'body': json.dumps({ "Answer": answer })
       }
