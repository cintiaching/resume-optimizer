# Resume Optimizer

A resume optimizer that tailors your resume to specific job descriptions. 
This tool is primarily for personal use to speed up my job application process, 
but feel free to use it as well. 
It is also a opportunity for me to build something and learn along the way, inspired by 
[5 AI Projects You Can Build This Weekend (with Python)](https://medium.com/towards-data-science/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461).

## Features

- Tailors resumes to match job descriptions.
  - Input: resume and job description
  - Output: optimized resume and explanation
- [Future] Generate cover letter given resume and job description.

## Roadmap

- [ ] Tailor the resume to the job descriptions.
  - [x] Input resume pdf, parse
  - [x] LLM api call, prompt engineering 
  - [ ] Output the optimized resume, in editable format
- [ ] Generate a cover letter based on the resume and job description.
- [ ] Implement a locally hosted frontend.

## Technologies used

- [marker](https://github.com/VikParuchuri/marker) Convert PDF to markdown + JSON quickly with high accuracy.
- [Ollama](https://ollama.com/) To run open source LLMs locally.


## Setup

To get started with the project, follow these steps:

1. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Set Up Ollama
   - Visit the [Ollama website](https://ollama.com) and download the installer.
   - Ollama will automatically start as a background service. If this feature is disabled, you can manually start it by running:
     ```bash
     ollama serve
     ```

3. After starting Ollama, download the required model from the Ollama model library by executing:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

4. You need to set the following environment variables, check .env.example
   ```bash
   RESUME_PATH=<put path here>
   JOB_DESC_PATH=<put path here>
   ```

5. Run the main script. The output will be printed to the console:
   ```bash
   python resume_optimizer.py
   ```
