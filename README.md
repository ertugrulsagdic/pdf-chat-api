pip install pipreqs
python -m  pipreqs.pipreqs .

create conda environment
conda create --name <env_name> python=3.10

conda activate <env_name>

if on macbook m chips run this command before running requirements.txt
conda install onnxruntime -c conda-forge

pip install -r requirements.txt