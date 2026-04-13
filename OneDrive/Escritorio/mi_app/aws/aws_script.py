import boto3
from datetime import datetime #importaciones

ec2 = boto3.resource('ec2', region_name='us-east-1')
s3 = boto3.client('s3')

def generar_reporte():
    nombre_archivo = "reporte_recursos.txt"
    print(f"Generando reporte en {nombre_archivo}")
    
    with open(nombre_archivo, "w") as f:
        f.write(f"REPORTE DE RECURSOS AWS - {datetime.now()}\n")
        f.write("="*40 + "\n\n")
        
        # Reporte de Instancias EC2
        f.write("--- INSTANCIAS EC2 ---\n")
        instancias = ec2.instances.all()
        count_ec2 = 0
        for i in instancias:
            linea = f"ID: {i.id} | Estado: {i.state['Name']} | Tipo: {i.instance_type}\n"
            f.write(linea)
            count_ec2 += 1
        f.write(f"Total de instancias: {count_ec2}\n\n")
        
        # Reporte de Buckets S3
        f.write("--- BUCKETS S3 ---\n")
        buckets = s3.list_buckets()['Buckets']
        for b in buckets:
            f.write(f"Nombre: {b['Name']}\n")
            # Listar objetos
            objs = s3.list_objects_v2(Bucket=b['Name'])
            for obj in objs.get('Contents', []):
                f.write(f"  - Objeto: {obj['Key']} ({obj['Size']} bytes)\n")
        f.write(f"Total de buckets: {len(buckets)}\n")
    
    print("Reporte generado con éxito!!!") #mensaje de confirmacion de que se creo el reporte bien

def crear_instancias(cantidad=1):
    if cantidad > 9: cantidad = 9
    print(f"Lanzando {cantidad} instancias...")
    ec2.create_instances(
        ImageId='ami-0c7217cdde317cfec',
        MinCount=1,
        MaxCount=cantidad,
        InstanceType='t3.micro',
        IamInstanceProfile={'Name': 'LabInstanceProfile'}
    )

if __name__ == "__main__":
    crear_instancias(1) 
    generar_reporte()