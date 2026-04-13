#!/bin/bash

# Nombres
STACK_NAME="MiProyectoStack"
TEMPLATE_FILE="infra_instancias.yaml"

echo "Iniciando el despliegue de CloudFormation: $STACK_NAME..."

#corre el comando de despliegue
aws cloudformation deploy \
  --template-file $TEMPLATE_FILE \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_NAMED_IAM

# Verifica si el comando anterior fue exitoso
if [ $? -eq 0 ]; then
  echo "Despliegue completado con éxito."
  echo " Estado actual del Stack:"
  aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].StackStatus" --output text
else
  echo "Error: El despliegue ha fallado"
  exit 1
fi