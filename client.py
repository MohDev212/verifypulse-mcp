import urllib.request
import json
from typing import Optional, Dict, Any

class VerifyPulseClient:
    """Client for the VerifyPulse B2B Email Deliverability & Verification Engine."""
    
    BASE_URL = "https://verifypulse-seven.vercel.app"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def verify_email(self, email: str, check_smtp: bool = False) -> Dict[str, Any]:
        """Verify a single email address for syntax, live MX records, and disposable status."""
        url = f"{self.BASE_URL}/v1/verify"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["X-API-Key"] = self.api_key

        data = json.dumps({"email": email, "check_smtp": check_smtp}).encode()
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())

    def inspect_dns(self, domain: str) -> Dict[str, Any]:
        """Inspect domain DNS for MX records, RFC 7208 SPF lookup limits, and DMARC alignment."""
        url = f"{self.BASE_URL}/api/inspect-dns?domain={domain}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())

    def auto_provision_agent(self, agent_id: str) -> Dict[str, Any]:
        """Self-provision a free API key with 100 credits for an autonomous AI agent."""
        url = f"{self.BASE_URL}/v1/agent/provision"
        data = json.dumps({"agent_id": agent_id}).encode()
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())


if __name__ == "__main__":
    client = VerifyPulseClient()
    print("Testing VerifyPulse DNS Inspection for stripe.com...")
    dns_res = client.inspect_dns("stripe.com")
    print("DNS Result:", dns_res)
