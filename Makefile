# Create pypi virtual env
create_env:
	@echo ">>> Create environment...\n"
	python3 -m venv main_env &&\
	source main_env/bin/activate && \
	python3 -m pip install -r requirements.txt && \
	python3 -m ipykernel install --user --name main_env_kernel
	@echo ">>> Environment successfully created!\n"
