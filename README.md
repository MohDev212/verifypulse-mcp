# VerifyPulse MCP Server & Agent Client

Public Model Context Protocol (MCP) server card and client interface for **VerifyPulse** (`https://verifypulse-seven.vercel.app`), which checks whether email will arrive: daily sending-domain monitoring, on-demand DNS audits and domain-level address checks, paid in USDC on Base over x402.

---

## What VerifyPulse does

- **Sending-domain audits**: MX, SPF with every include expanded and the true lookup count, DMARC policy and DKIM keys
- **Daily monitoring**: signed webhook alerts when a domain's SPF, DKIM, DMARC, MX or MTA-STS changes
- **Bulk-sender checks**: a domain's DNS against the Gmail and Yahoo SPF, DKIM and DMARC requirements
- **Domain age and TLS checks**: RDAP registration data and certificate status
- **Address checks**: RFC 5322 syntax, the domain's MX records, typos, and disposable and shared-mailbox flags

### What it does not do

Address checks are domain-level. VerifyPulse does not offer mailbox verification and cannot confirm that a specific inbox exists. `GET /v1/x402/verify-email` runs no SMTP probe and reports `smtp_check: not_performed`. The MCP `verify_email` tool may attempt one, but the hosting platform commonly filters outbound port 25, so a mailbox result cannot be promised.

---

## Remote MCP server (Streamable HTTP)

Connect any MCP client that supports remote servers:

```json
{
  "mcpServers": {
    "verifypulse": {
      "type": "http",
      "url": "https://verifypulse-seven.vercel.app/mcp"
    }
  }
}
```

- **Endpoint**: `POST https://verifypulse-seven.vercel.app/mcp`
- **Protocol**: JSON-RPC 2.0 (Model Context Protocol), no key needed to connect

---

## x402 payments on Base Mainnet

- **Network**: Base Mainnet (`eip155:8453`)
- **Token**: USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
- **Recipient**: `0x42871B99A3AA942D3B8EC7E43D37979886E856cA`
- **Facilitators**: `https://facilitator.xpay.sh`, then `https://facilitator.payai.network` (`POST /settle`)
- **Direct**: a recent Base USDC transfer hash to the recipient in `X-PAYMENT` or `X-Payment-TxHash`, redeemable once

### Per call

| Endpoint | Price (USDC) |
|---|---|
| `GET /v1/x402/verify-email?email=name@example.com` | $0.01 |
| `GET /v1/x402/dns-audit?domain=example.com` | $0.01 |
| `GET /v1/x402/compliance-dmarc?domain=example.com` | $0.01 |
| `GET /v1/x402/domain-health?domain=example.com` | $0.01 |
| `GET /v1/x402/guard-audit?domains=a.com,b.com` (up to 20) | $0.02 |
| `GET /v1/x402/domain-intel?domains=a.com,b.com` (up to 20) | $0.02 |
| `GET /v1/x402/tls-check?hosts=a.com,b.com` (up to 20) | $0.02 |
| `GET /v1/x402/fix-kit?domain=example.com` | $0.25 |

### One-time purchases (nothing renews)

| Endpoint | Price (USDC) | Buys |
|---|---|---|
| `GET /v1/x402/credits?pack=1000` | $1.00 | 1,000 credits |
| `GET /v1/x402/credits?pack=5000` | $5.00 | 5,000 credits |
| `GET /v1/x402/guard-pass?plan=guard_starter` | $2.00 | 30 days, 50 domains |
| `GET /v1/x402/guard-pass?plan=guard_agency` | $5.00 | 30 days, 300 domains |
| `GET /v1/x402/guard-pass?plan=guard_scale` | $12.00 | 30 days, 1,500 domains |

Current prices are always in the [OpenAPI document](https://verifypulse-seven.vercel.app/openapi.json) and [pricing.json](https://verifypulse-seven.vercel.app/pricing.json).

---

## Quick start (Python)

Sending-domain audits are free for up to 3 domains per call, with no key:

```python
import json
import urllib.request

req = urllib.request.Request(
    "https://verifypulse-seven.vercel.app/v1/guard/audit",
    data=json.dumps({"domains": ["github.com"]}).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as resp:
    print(json.loads(resp.read().decode()))
```

---

## Links

- **Live service**: [https://verifypulse-seven.vercel.app](https://verifypulse-seven.vercel.app)
- **OpenAPI**: [https://verifypulse-seven.vercel.app/openapi.json](https://verifypulse-seven.vercel.app/openapi.json)
- **x402 discovery**: [https://verifypulse-seven.vercel.app/.well-known/x402](https://verifypulse-seven.vercel.app/.well-known/x402)
- **Support**: [GitHub issues](https://github.com/MohDev212/verifypulse-mcp/issues)
- **Maintainer**: [MohDev212](https://github.com/MohDev212)
