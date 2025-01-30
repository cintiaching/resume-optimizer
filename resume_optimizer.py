import os
from dotenv import load_dotenv

from optimizer.text_processing import convert_pdf_to_markdown
from optimizer.llm import llm_chat, LLMs

# Load environment variables from .env file
load_dotenv()

resume_path = os.environ.get("RESUME_PATH")
job_desc_path = os.environ.get("JOB_DESC_PATH")

# raise error if path not found
if resume_path is None or job_desc_path is None:
    raise ValueError(f"Please set both RESUME_PATH and JOB_DESC_PATH as environment variables")

# convert to markdown
resume_markdown = convert_pdf_to_markdown(resume_path)
jd_markdown = convert_pdf_to_markdown(job_desc_path)

prompt = f"""
I have a resume formatted in Markdown and a job description. \
Please adapt my resume to better align with the job requirements while \
maintaining a professional tone. Tailor my skills, experiences, and \
achievements to highlight the most relevant points for the position. \
Ensure that my resume still reflects my unique qualifications and strengths \
but emphasizes the skills and experiences that match the job description.

### Here is my resume in Markdown:
{resume_markdown}

### Here is the job description:
{jd_markdown}

### Important Instruction
Please modify the resume to:
- Use keywords and phrases from the job description.
- Adjust the bullet points under each role to emphasize relevant skills and achievements.
- Make sure my experiences are presented in a way that matches the required qualifications.
- Maintain clarity, conciseness, and professionalism throughout.

Please think and answer everything in English. Do not make up qualification that is not in the original resume.
Return the updated resume in Markdown format.
"""

output = llm_chat(prompt, LLMs.DEEPSEEK_R1)
print(output)
