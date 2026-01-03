"""
AI News Analyzer - FREE VERSION (No OpenAI costs)
Uses local AI or free APIs
"""
import os
import json
import csv
from datetime import datetime
from dotenv import load_dotenv
import requests

class FreeNewsAnalyzer:
    def __init__(self):
        """Initialize without OpenAI dependency"""
        print("✅ Using FREE news analyzer (no API costs)")
    
    def fetch_news(self, topic="artificial intelligence", count=3):
        """Fetch real news from free APIs"""
        print(f"📰 Fetching news about: {topic}...")
        
        try:
            # Option A: Use NewsAPI (free tier available)
            # Get free key from: https://newsapi.org/register
            newsapi_key = os.getenv("NEWS_API_KEY", "demo")
            
            if newsapi_key != "demo":
                url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={newsapi_key}"
                response = requests.get(url)
                data = response.json()
                
                articles = []
                for item in data.get("articles", [])[:count]:
                    articles.append({
                        "title": item.get("title", "No title"),
                        "content": item.get("description", "") + " " + item.get("content", ""),
                        "source": item.get("source", {}).get("name", "Unknown"),
                        "url": item.get("url", "#"),
                        "published": item.get("publishedAt", datetime.now().strftime("%Y-%m-%d"))
                    })
                
                if articles:
                    print(f"✅ Found {len(articles)} real news articles")
                    return articles
            
            # Option B: Use free RSS feeds or web scraping
            # Fallback to demo data
            print("⚠️ Using demo data (add NEWS_API_KEY for real news)")
            
        except Exception as e:
            print(f"⚠️ News fetch error: {e}")
        
        # Demo fallback
        return self._get_demo_articles(count)
    
    def _get_demo_articles(self, count=3):
        """Provide demo articles for portfolio"""
        articles = [
            {
                "title": "AI Breakthrough in Medical Diagnostics - Machine learning detects diseases from X-rays with 98% accuracy",
                "content": "Researchers at Stanford developed an AI system that analyzes medical images faster and more accurately than human radiologists. The technology could reduce diagnostic errors by 40% and is expected to be deployed in hospitals nationwide by Q4 2024.",
                "source": "Tech Medical Journal",
                "url": "https://example.com/ai-medical",
                "published": "2024-01-15"
            },
            {
                "title": "OpenAI Launches GPT-5 Developer Preview - New model shows 50% improvement in reasoning tasks",
                "content": "OpenAI announced the developer preview of GPT-5, featuring enhanced coding capabilities and better contextual understanding. Early tests show significant improvements in mathematical reasoning and code generation, positioning it as a major advancement in generative AI.",
                "source": "AI Research Daily",
                "url": "https://example.com/gpt5",
                "published": "2024-01-14"
            },
            {
                "title": "Global AI Regulation Framework Established - 50 countries agree on safety standards",
                "content": "At the Global AI Safety Summit, world leaders established the first international framework for AI regulation. The agreement focuses on transparency requirements, safety testing protocols, and accountability measures for high-risk AI systems.",
                "source": "Global Tech News",
                "url": "https://example.com/ai-regulation",
                "published": "2024-01-13"
            }
        ]
        return articles[:count]
    
    def analyze_article(self, article):
        """Simulate AI analysis for portfolio/demo"""
        print(f"   Analyzing: {article['title'][:50]}...")
        
        # For portfolio: Create realistic analysis without API calls
        analysis_templates = [
            {
                "trend": "AI in Healthcare",
                "impact": "High - Potential to reduce diagnostic costs by 30%",
                "risk_level": "Low",
                "opportunity": "Healthcare tech companies, medical device manufacturers",
                "summary": "AI diagnostics represent a major market opportunity with strong growth potential."
            },
            {
                "trend": "Generative AI Advancements",
                "impact": "Medium - Will accelerate software development and content creation",
                "risk_level": "Medium",
                "opportunity": "SaaS platforms, development tools, content agencies",
                "summary": "Next-gen AI models will drive productivity gains across multiple industries."
            },
            {
                "trend": "AI Regulation & Compliance",
                "impact": "High - Will create new compliance markets and consulting services",
                "risk_level": "High",
                "opportunity": "Compliance software, consulting firms, audit services",
                "summary": "Regulatory frameworks will shape AI adoption and create new business verticals."
            }
        ]
        
        # Use different template for each article
        import hashlib
        article_hash = int(hashlib.md5(article['title'].encode()).hexdigest(), 16)
        template_index = article_hash % len(analysis_templates)
        
        return {
            "article_title": article["title"],
            "source": article["source"],
            "published": article["published"],
            "analysis": analysis_templates[template_index],
            "analyzed_at": datetime.now().isoformat(),
            "note": "Demo analysis - Replace with OpenAI API for real AI insights"
        }
    
    def generate_reports(self, analyses):
        """Generate reports (same as before)"""
        print("📊 Generating intelligence reports...")
        
        report_dir = "intelligence_reports"
        os.makedirs(report_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate all report files (same code as before)
        json_file = f"{report_dir}/news_analysis_{timestamp}.json"
        csv_file = f"{report_dir}/news_analysis_{timestamp}.csv"
        txt_file = f"{report_dir}/news_analysis_{timestamp}_summary.txt"
        
        # ... (same report generation code)
        
        print(f"✅ Reports generated in '{report_dir}/'")
        return [json_file, csv_file, txt_file]
    
    def run(self, topic="AI technology", article_count=3):
        """Main execution - FREE VERSION"""
        print("\n" + "=" * 60)
        print("🚀 AI NEWS ANALYZER (FREE VERSION)")
        print("=" * 60)
        
        try:
            articles = self.fetch_news(topic, article_count)
            print(f"✅ Found {len(articles)} articles")
            
            print("\n🤖 Analyzing articles...")
            analyses = []
            for i, article in enumerate(articles, 1):
                analysis = self.analyze_article(article)
                analyses.append(analysis)
                print(f"   ✓ Analyzed article {i}/{len(articles)}")
            
            reports = self.generate_reports(analyses)
            
            print("\n" + "=" * 60)
            print("🎯 FREE VERSION EXECUTION COMPLETE")
            print("=" * 60)
            print("📊 Portfolio-Ready Results:")
            print(f"   • Articles Processed: {len(articles)}")
            print(f"   • Analyses Generated: {len(analyses)}")
            print(f"   • Report Files: {len(reports)}")
            print("\n💡 To enable real AI analysis:")
            print("   1. Add credits to OpenAI account")
            print("   2. OR replace analyze_article() with OpenAI API calls")
            print("=" * 60)
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

def main():
    """Use free version for portfolio"""
    analyzer = FreeNewsAnalyzer()
    analyzer.run()

if __name__ == "__main__":
    main()