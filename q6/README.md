# Write a kubernetes (preferably helm) template that deploys nginx with custom configuration and exposes services as NodePort 

## Solution  
1. create an basic helm chart with `helm create nginx`.
2. replace [targetPort](nginx/templates/service.yaml#L11) in service template with variable.  
3. add default value for [targetPort](nginx/values.yaml#L42) in values.yaml.
4. add [template for configmap](nginx/templates/configmap.yaml) from conf.d that will hold custom nginx configurations.
5. modify template for deployment to define [volume](nginx/templates/deployment.yaml#L30) and [volumeMount](nginx/templates/deployment.yaml#L35)  
6. check syntax with `helm lint nginx`  
