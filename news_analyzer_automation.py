"""
AI News Analyzer Automation - Secure Version
Fetches news, analyzes with AI, generates reports
"""
import os
import json
import csv
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

class NewsAnalyzer:
    def __init__(self):
        # Secure API key loading
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ OPENAI_API_KEY not found in .env file")
        
        self.client = OpenAI(api_key=self.api_key)
        self.news_api_key = os.getenv("NEWS_API_KEY", "demo_key")
        
    def fetch_news(self, query="artificial intelligence", num_articles=5):
        """Fetch news articles from NewsAPI"""
        print(f"📰 Fetching news about: {query}...")
        
        # Demo data (replace with real API call)
        demo_articles = [
            {
                "title": "AI Revolutionizes Healthcare Diagnostics",
                "content": "New AI systems can detect diseases earlier than human doctors...",
                "source": "Tech News",
                "url": "https://example.com/ai-health",
                "published": "2024-01-15"
            },
            {
                "title": "OpenAI Releases GPT-5 Preview",
                "content": "The latest model shows 50% improvement in reasoning tasks...",
                "source": "AI Daily",
                "url": "https://example.com/gpt5",
                "published": "2024-01-14"
            },
            {
                "title": "AI Regulation Debated in Congress",
                "content": "Lawmakers discuss balancing innovation with safety concerns...",
                "source": "Politics Today",
                "url": "https://example.com/ai-law",
                "published": "2024-01-13"
            }
        ]
        
        return demo_articles[:num_articles]
    
    def analyze_with_ai(self, articles):
        """Analyze news articles using OpenAI"""
        print("🤖 Analyzing with AI...")
        
        insights = []
        for article in articles:
            try:
                # Create analysis prompt
                prompt = f"""
                Analyze this news article for market intelligence:
                
                Title: {article['title']}
                Content: {article['content'][:500]}...
                
                Provide:
                1. Key trend identified
                2. Potential market impact
                3. Risk assessment
                4. Business opportunity
                
                Format as JSON with: trend, impact, risk, opportunity
                """
                
                # Call OpenAI API (new version syntax)
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a market intelligence analyst."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=500
                )
                
                analysis = response.choices[0].message.content
                
                # Try to parse JSON, fallback to text
                try:
                    analysis_data = json.loads(analysis.strip())
                except:
                    analysis_data = {"insight": analysis}
                
                insights.append({
                    "article": article["title"],
                    "analysis": analysis_data,
                    "source": article["source"],
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                print(f"⚠️ Analysis error: {e}")
                insights.append({
                    "article": article["title"],
                    "analysis": {"error": str(e)},
                    "source": article["source"]
                })
        
        return insights
    
    def generate_reports(self, insights):
        """Generate JSON, CSV, and TXT reports"""
        print("📊 Generating reports...")
        
        # Create reports directory
        report_dir = "news_intelligence_reports"
        os.makedirs(report_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 1. JSON Report
        json_file = f"{report_dir}/news_analysis_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(insights, f, indent=2)
        
        # 2. CSV Report
        csv_file = f"{report_dir}/news_analysis_{timestamp}.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Article', 'Trend', 'Impact', 'Risk', 'Opportunity', 'Source', 'Timestamp'])
            
            for insight in insights:
                analysis = insight['analysis']
                writer.writerow([
                    insight['article'],
                    analysis.get('trend', 'N/A'),
                    analysis.get('impact', 'N/A'),
                    analysis.get('risk', 'N/A'),
                    analysis.get('opportunity', 'N/A'),
                    insight['source'],
                    insight.get('timestamp', 'N/A')
                ])
        
        # 3. TXT Insights Summary
        txt_file = f"{report_dir}/news_analysis_{timestamp}_insights.txt"
        with open(txt_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write("AI NEWS INTELLIGENCE REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            for i, insight in enumerate(insights, 1):
                f.write(f"ARTICLE {i}: {insight['article']}\n")
                f.write(f"Source: {insight['source']}\n")
                f.write("-"*40 + "\n")
                
                analysis = insight['analysis']
                for key, value in analysis.items():
                    f.write(f"{key.upper()}: {value}\n")
                
                f.write("\n" + "="*60 + "\n\n")
        
        print(f"✅ Reports saved in '{report_dir}' folder:")
        print(f"   - {json_file}")
        print(f"   - {csv_file}")
        print(f"   - {txt_file}")
        
        return [json_file, csv_file, txt_file]
    
    def run_analysis(self, query="AI technology", num_articles=3):
        """Main execution method"""
        print("🚀 Starting AI News Analyzer Automation...")
        print("="*60)
        
        try:
            # 1. Fetch news
            articles = self.fetch_news(query, num_articles)
            print(f"✅ Fetched {len(articles)} articles")
            
            # 2. Analyze with AI
            insights = self.analyze_with_ai(articles)
            print(f"✅ Generated {len(insights)} AI insights")
            
            # 3. Generate reports
            reports = self.generate_reports(insights)
            
            # 4. Display summary
            print("\n" + "="*60)
            print("🎯 AUTOMATION EXECUTION COMPLETE")
            print("="*60)
            print(f"Articles Analyzed: {len(articles)}")
            print(f"AI Insights Generated: {len(insights)}")
            print(f"Reports Created: {len(reports)} files")
            print(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\n📈 PORTFOLIO VALUE DEMONSTRATED:")
            print("- Automated market intelligence pipeline")
            print("- AI-powered trend analysis")
            print("- Structured multi-format reporting")
            print("- Production-ready error handling")
            print("="*60)
            
        except Exception as e:
            print(f"❌ Critical error: {e}")
            return None

def main():
    """Main entry point"""
    analyzer = NewsAnalyzer()
    analyzer.run_analysis()

if __name__ == "__main__":
    main()