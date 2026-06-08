Build 2 — Plain Text Summarizer
A Python script that makes an Anthropic call by pulling the key from a .env file and keeps it secure and safe and then reads a text file to and ask Anthropic to summarize the file.

Setup
1. pip install anthropic pyton-dotenv
2. Create a .env file with your Anthropic API key:
   ANTHROPIC_API_KEY=your_key_here
3. Create sample.txt file with any text you want summarized
Run it
Create a sample.txt file and run the script. The script will summarize your text file.

python summarizer.py
Example:

Sample.txt file
"Executive Brief: Artificial Intelligence in Modern HealthcareThe integration of artificial intelligence (AI) into global healthcare systems is accelerating at an unprecedented pace. Industry analysts estimate that the global market for healthcare AI will surpass $100 billion by 2030, driven largely by advancements in deep learning models and natural language processing. Currently, the most significant operational impact is seen in medical imaging and diagnostics. Machine learning algorithms can analyze X-rays, MRIs, and CT scans with accuracy rates that rival or occasionally exceed senior radiologists, particularly in the early detection of malignant tumors and cardiovascular anomalies. By automating these preliminary screenings, hospitals report a 30% reduction in diagnostic turnaround times, allowing physicians to initiate patient treatments much faster.Beyond diagnostics, AI is transforming patient administrative workflows and chronic disease management. Hospitals are deploying conversational AI tools to handle patient triaging, appointment scheduling, and automated follow-ups for post-operative care. This shift addresses a critical challenge in modern medicine: administrative burnout among clinical staff. Surveys indicate that nurses and doctors spend up to 25% of their shifts completing paperwork. Automated documentation tools drastically cut this administrative burden, restoring valuable hours back to direct, face-to-face patient care. Furthermore, predictive analytics models are now utilized to forecast patient admission rates, optimizing hospital staffing and resource allocation during peak seasons.However, the widespread adoption of medical AI introduces severe ethical, technical, and regulatory challenges that hospital boards must address immediately. The primary concern is data privacy; training robust AI models requires massive datasets of sensitive patient information, increasing the risk of data breaches and violations of regulations like HIPAA. Additionally, algorithmic bias remains a critical flaw. If an AI model is trained predominantly on data from affluent demographics, its diagnostic accuracy drops significantly when applied to underrepresented patient populations. To mitigate these risks, regulatory bodies are mandating stricter validation protocols. Healthcare providers are advised to establish strict data governance committees and require algorithmic transparency from their software vendors before deploying any patient-facing AI tools.

Script Return:
"## Summary: AI in Modern Healthcare

**Market Growth & Diagnostics**
The healthcare AI market is projected to exceed $100 billion by 2030, fueled by deep learning and natural language processing. The biggest current impact is in medical imaging, where algorithms analyze X-rays, MRIs, and CT scans with accuracy rivaling senior radiologists—especially in detecting tumors and cardiovascular issues. This has reduced diagnostic turnaround times by 30%.

**Administrative & Operational Benefits**
AI is also transforming workflows by handling patient triaging, scheduling, and post-operative follow-ups. Since clinical staff spend up to 25% of shifts on paperwork, automated documentation reduces administrative burnout and returns time to patient care. Predictive analytics further help forecast admissions and optimize staffing.

**Key Challenges & Risks**
Widespread adoption raises significant concerns:
- **Data Privacy:** Large datasets of sensitive patient information increase breach risks and potential HIPAA violations.
- **Algorithmic Bias:** Models trained on non-diverse data show reduced accuracy for underrepresented populations.

**Recommendations**
Regulators are imposing stricter validation protocols. Healthcare providers should establish data governance committees and require algorithmic transparency from vendors before deploying patient-facing AI tools."

What I took away
- I was able to make call through API and keep the API Key secure by using .env and .gitignore
- Learned how virtual environments work and why Python version conflicts happen
- Learned that .env variable names must exactly match what you call in os.getenv()
- Learned what the full API response object looks like and how to extract the text with message.content[0].text
