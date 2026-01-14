# singing-materials-online

To install, follow these setup instructions:

**Step 1: Install Python Libraries**

In a clean conda environment:
```
conda install anaconda::flask
conda install anaconda::jupyter
conda install conda-forge::python-dotenv
conda install conda-forge::mp-api
```

Note: pip install is difficult on some systems as a `mp-api` dependency, `spglib`, might then be required to be built from source, and can fail due to not having correct C library headers. `conda` works around this as it does not require any building from source.

**Step 2: Setup a .env file**

In the project root create a `.env` file. This contains your personal API key for communicating with the Materials Project database. You API key is available [here](https://next-gen.materialsproject.org/api) (you need to sign up for an account first). Store as `export MP-API-KEY="xxxxxxxxxx"`.

**Step 3: Run the Flask App**
`python app.py`

**Step 4: Access the web application in a browser**
 The web application can be accessed in a browser via `http://127.0.0.1:5000/`
