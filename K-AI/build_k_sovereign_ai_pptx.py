# -*- coding: utf-8 -*-
"""
Dell 총판 제안서 템플릿(Dell_Distibutor_proposal.pptx)을 기반으로
UCLA Anderson Executive MBA 내방용 30슬라이드 공식 PowerPoint (.pptx) 프레젠테이션 덱 생성기
- 작성일자: 2026-09-09
- 발표자: Andy (ISV Business Unit & AI Architecture Group, MegazoneCloud)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_sovereign_ai_pptx():
    output_path = r"c:\dev\antigravity-workspace\aifullstack\K-AI\2026-09-09_Korea_Sovereign_AI_Strategy_Deck.pptx"
    img_dir = r"c:\dev\antigravity-workspace\aifullstack\K-AI\images"

    # 새 프레젠테이션 생성 (16:9 와이드스크린 13.33 x 7.5 인치)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 컬러 팔레트 정의 (UCLA Navy/Gold + MegazoneCloud Tech Blue)
    COLOR_NAVY_DARK = RGBColor(0, 43, 73)      # #002B49
    COLOR_NAVY_MED = RGBColor(0, 59, 92)       # #003B5C
    COLOR_GOLD = RGBColor(255, 209, 0)         # #FFD100
    COLOR_MZC_BLUE = RGBColor(0, 102, 255)     # #0066FF
    COLOR_MZC_CYAN = RGBColor(0, 194, 255)     # #00C2FF
    COLOR_TEXT_MAIN = RGBColor(30, 41, 59)     # #1E293B
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # #64748B
    COLOR_CARD_BG = RGBColor(248, 250, 252)    # #F8FAFC
    COLOR_CARD_BORDER = RGBColor(226, 232, 240)# #E2E8F0
    COLOR_WHITE = RGBColor(255, 255, 255)

    # 30개 슬라이드 전체 데이터 정의
    slides_data = [
        {
            "num": 1,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "Korea's Sovereign AI Strategy: From Silicon to Enterprise Applications",
            "subtitle": "Unlocking Strategic Autonomy, Native Infrastructure, and Scalable Enterprise Transformation",
            "image": os.path.join(img_dir, "slide01_cover_sovereign_ai.jpg"),
            "bullets": [
                ("Welcome to MegazoneCloud", "Executive visit to Gwacheon HQ for UCLA Anderson EMBA Seoul Immersion 2026."),
                ("One of Only 3 Global AI Powerhouses", "South Korea uniquely pairs world-leading semiconductor memory (HBM) with native hyperscale digital engines and foundation models."),
                ("Beyond Models to Operational Sovereignty", "Orchestrating domestic NPU silicon, specialized foundation models, and enterprise full-stack orchestration.")
            ],
            "visual": "Futuristic visual blending Seoul skyline, AI neural nodes, and enterprise server racks.",
            "notes": "Good morning, faculty, staff, and distinguished executives of the UCLA Anderson Executive MBA delegation. On behalf of MegazoneCloud, welcome to our Gwacheon Headquarters. Today, I am thrilled to share South Korea's sovereign AI playbook—how our nation is navigating the global AI race by building independent silicon, specialized models, and full-stack enterprise solutions.",
            "duration": "0:00 - 0:30"
        },
        {
            "num": 2,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "Welcome UCLA Anderson EMBA: Objectives & Agenda",
            "subtitle": "Today's 15-Minute Executive Briefing & Collaborative Exchange",
            "bullets": [
                ("Strategic Understanding", "Deconstruct the geopolitical, financial, and technical forces driving Sovereign AI in 2026."),
                ("The 4-Pillar Playbook", "Deep-dive into Infrastructure, Models, Software Solutions, and Enterprise Services."),
                ("MegazoneCloud's Role", "Scaling from Korea's #1 Cloud Unicorn to the master orchestrator of domestic and global ISVs."),
                ("Connecting Your Itinerary", "Direct synergy with your Seoul immersion: Samsung, DEEPX, Amorepacific, and Invest Seoul.")
            ],
            "visual": "Flow diagram showing 3-stage presentation breakdown and interactive Q&A roadmap.",
            "notes": "Over the next 15 minutes, we will unpack why sovereign AI is an urgent commercial reality and how Korea provides an actionable template for global enterprise leaders.",
            "duration": "0:30 - 1:00"
        },
        {
            "num": 3,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The Geopolitics of AI: Why 'Sovereignty' Matters in 2026",
            "subtitle": "From AI Experimentation to Strategic Operational Autonomy",
            "bullets": [
                ("The AI Duopoly Threat", "Over-reliance on foreign hyperscalers exposes enterprises to price volatility, unexpected outages, and deep vendor lock-in."),
                ("Sovereign AI 2.0 Defined", "Moving beyond 'owning a model' to 'Operational Sovereignty' and 'Access Autonomy'—ensuring mission-critical workflows run offline."),
                ("Regulatory Compliance Mandates", "Strict cross-border data residency mandates (EU AI Act, Korea PIPA, Financial Cloud Directives).")
            ],
            "visual": "Comparison matrix: Cloud SaaS API Risks vs. Air-Gapped Sovereign AI Enterprise Benefits.",
            "notes": "In 2026, the question is no longer 'Which API is smartest?' but 'Who owns our intelligence? If cross-border connections drop, can our business still operate?'",
            "duration": "1:00 - 1:30"
        },
        {
            "num": 4,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "South Korea’s Unique Position: The World’s 3rd AI Powerhouse",
            "subtitle": "A Rare Convergence of Semiconductor, Software, and Heavy Industry",
            "bullets": [
                ("Elite Global Trio", "Alongside the US and China, South Korea possesses the complete physical and digital vertical stack."),
                ("Hardware Dominance", "Global leader in memory and HBM manufacturing (Samsung Electronics, SK Hynix)."),
                ("Digital Platforms & Models", "Domestic tech giants (Naver, Kakao) beating global platforms locally with native search engines."),
                ("The 'G3 Ambition'", "Formal presidential roadmap targeting Global Top 3 AI leadership by 2027.")
            ],
            "visual": "Global map highlighting US, China, and Korea with 4-layer full-stack capability indicators.",
            "notes": "Korea possesses the entire physical and digital vertical stack. We build the memory chips, host native search engines, and manufacture ships, cars, and consumer electronics.",
            "duration": "1:30 - 2:00"
        },
        {
            "num": 5,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The Enterprise Trilemma: Capex, Power, and Data Sovereignty",
            "subtitle": "The Hard Physical Bottlenecks Stalling On-Premises Deployments",
            "bullets": [
                ("Financial Shock (Capex)", "8-GPU high-density servers cost $400K-$500K each with unpredictable delivery cycles."),
                ("Physical Power Cap", "90% of corporate datacenter racks are limited to 8-10kW; standard 8-GPU servers draw 10.2kW peak."),
                ("Data Exfiltration Risk", "Defense, banking, and semiconductor fabs strictly forbid transmitting IP to public clouds.")
            ],
            "visual": "Trilemma diagram: High Capex vs. 10kW Rack Power Limit vs. Air-Gapped Security Requirements.",
            "notes": "When enterprise CTOs attempt to run 250B parameter models on-premises, they hit an electrical brick wall. Overcoming this physical trilemma is our primary engineering focus.",
            "duration": "2:00 - 2:30"
        },
        {
            "num": 6,
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The 4-Pillar Framework: Infra, Model, Solution, Service",
            "subtitle": "The Unified Architecture of National & Enterprise AI Independence",
            "bullets": [
                ("Pillar 1 (Infrastructure)", "Compute clusters, public AI highway, and native NPU semiconductors."),
                ("Pillar 2 (Model)", "Sovereign Korean foundation models, domain sLLMs, and Mixture-of-Experts (MoE)."),
                ("Pillar 3 (Solution)", "Full-stack orchestration, air-gapped security, and model optimization compilers."),
                ("Pillar 4 (Service)", "Cross-industry deployment across Chaebols, SMEs, and public administrative sectors.")
            ],
            "visual": "4-Layer architectural pyramid highlighting synchronized execution across government and private sector.",
            "notes": "Sovereignty fails if any single layer is missing. Korea's strategy coordinates all 4 pillars synchronously to deliver commercial and operational success.",
            "duration": "2:30 - 3:00"
        },
        {
            "num": 7,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "National AI Computing Center: The Public-Private 'AI Highway'",
            "subtitle": "A Multi-Billion Dollar Sovereign Compute Megaproject",
            "image": os.path.join(img_dir, "slide07_infra_knpu_datacenter.jpg"),
            "bullets": [
                ("Solaseado Datacenter Park", "Officially broken ground in August 2026 in Haenam, South Jeolla Province."),
                ("Public-Private Consortium", "Spearheaded by MSIT and Samsung SDS via a dedicated Special Purpose Company (SPC)."),
                ("National Compute Bedrock", "Subsidizing massive compute access for universities, startups, and domestic industry.")
            ],
            "visual": "Architectural rendering of Haenam Solaseado datacenter campus with green energy grid connections.",
            "notes": "Pillar 1 begins with compute. In August 2026, Korea broke ground on the National AI Computing Center in Haenam, ensuring domestic industry is protected from international GPU supply crunches.",
            "duration": "3:00 - 3:30"
        },
        {
            "num": 8,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Compute Capacity Scaling: 15,000 GPUs to 50,000 GPUs",
            "subtitle": "The Exponential Trajectory of Public Compute Infrastructure",
            "bullets": [
                ("Phase 1 (2026 - 2028)", "Initial deployment of 15,000 top-tier AI accelerators (H100/B200 tier)."),
                ("Phase 2 (2029 - 2030+)", "Expansion to 50,000+ accelerators integrated with coastal offshore wind power."),
                ("Sovereign Resource Allocation", "Tiered vouchers enabling rapid model training without predatory cloud pricing.")
            ],
            "visual": "Growth chart showing GPU capacity scaling from 15K to 50K units by 2030 with power efficiency curves.",
            "notes": "Reaching 15,000 accelerators by 2028 and 50,000 by 2030 establishes a fortress of compute capacity that underpins national digital sovereignty.",
            "duration": "3:30 - 4:00"
        },
        {
            "num": 9,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "The Rise of K-NPU: The 'K-Cloud' Initiative & NPU Farms",
            "subtitle": "Disrupting the AI Inference Landscape with High-Efficiency Silicon",
            "bullets": [
                ("K-Cloud Initiative", "Over $600M in national backing to develop ultra-low-power AI semiconductors."),
                ("The 80/20 Rule", "While model training requires GPUs, over 80% of operational enterprise TCO is inference."),
                ("NPU Farms in Action", "Live multi-petaflop clusters deployed across Naver, KT, and NHN Cloud datacenters.")
            ],
            "visual": "Inference TCO comparison: K-NPU vs. Traditional GPU showing power and cost savings.",
            "notes": "Up to 80% of enterprise AI costs are inference. Korea's K-Cloud project deploys native NPUs specifically engineered to execute inference at a fraction of standard GPU power.",
            "duration": "4:00 - 4:30"
        },
        {
            "num": 10,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Korea's Fabless Champions: Rebellions, FuriosaAI, DEEPX, Mobilint",
            "subtitle": "Purpose-Built Silicon Across Datacenter, Edge, and Robotics",
            "bullets": [
                ("Rebellions (ATOM / ATOM-MAX)", "High-throughput datacenter inference and financial algorithmic trading."),
                ("FuriosaAI (WARBOY / RENEGADE)", "High-efficiency computer vision and Transformer model acceleration."),
                ("DEEPX (All-in-4 AI Series)", "Ultra-low-power on-device NPU for smart mobility, IoT, and industrial robotics (On UCLA Itinerary!)."),
                ("Mobilint (ARIES / REGULUS)", "Edge AI solutions for industrial automation.")
            ],
            "visual": "Silicon ecosystem landscape mapping Korean fabless startups across Datacenter, Edge, and On-Device tiers.",
            "notes": "Many of you are visiting DEEPX this week. DEEPX, Rebellions, and FuriosaAI are not mimicking GPUs; they are building purpose-driven architectures that win on efficiency.",
            "duration": "4:30 - 5:00"
        },
        {
            "num": 11,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Enterprise Hybrid Cloud & GPUaaS: Dell, NVIDIA, and Akamai",
            "subtitle": "Balancing Tier-1 Global Standards with Modular Sovereign Clouds",
            "bullets": [
                ("Mainstream Enterprise Track", "Dell PowerEdge R760 + NVIDIA GPUs for on-premise high performance."),
                ("Cost-Optimized GPUaaS", "Partnership with Akamai Distributed Cloud for sub-millisecond edge inferencing at 40% lower egress."),
                ("Hybrid Topology", "Sensitive proprietary IP kept strictly on-premises; public workloads burst to sovereign cloud.")
            ],
            "visual": "Hybrid network architecture showing Dell On-Premises core connected to Akamai GPUaaS edge nodes.",
            "notes": "Sovereignty is not isolation. MegazoneCloud delivers certified Dell and NVIDIA enterprise stacks while leveraging distributed GPUaaS partnerships like Akamai to optimize client TCO.",
            "duration": "5:00 - 5:30"
        },
        {
            "num": 12,
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Overcoming Data Center Bottlenecks: 10kW Rack Power & Cooling",
            "subtitle": "Engineering Feasibility in Existing Corporate Server Rooms",
            "bullets": [
                ("The Datacenter Bottleneck", "Retrofitting legacy server rooms with liquid cooling costs millions and causes downtime."),
                ("Dense 2-GPU Form Factor", "High-efficiency 2U dual-GPU architecture delivering enterprise-grade throughput."),
                ("Power Feasibility", "Operating power capped at 3.2kW, safely within standard 10kW datacenter rack limits.")
            ],
            "visual": "Server rack diagram showing 3.2kW 2-GPU server fitting comfortably into standard 10kW rack space.",
            "notes": "Our dual-GPU dense form factor caps power draw at 3.2kW. Enterprises can deploy sovereign AI in their existing server rooms tomorrow without electrical rewiring.",
            "duration": "5:30 - 6:00"
        },
        {
            "num": 13,
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Korea's Foundation Model Landscape",
            "subtitle": "Native Linguistic Mastery and Frontier Enterprise Intelligence",
            "bullets": [
                ("Naver HyperCLOVA X", "Dominant commercial hyper-scale model trained on 6,500x more Korean data than GPT-3."),
                ("LG AI Research EXAONE 3.0", "High-performance bilingual open-weight model engineered for chemistry, patents, and manufacturing."),
                ("Upstage Solar", "Globally acclaimed sLLM leading HuggingFace benchmarks via innovative Depth-Up Scaling (DUS).")
            ],
            "visual": "Logo and performance matrix comparing HyperCLOVA X, EXAONE 3.0, and Solar across enterprise benchmarks.",
            "notes": "Pillar 2: Models. Korea does not rely solely on translated foreign LLMs. Naver, LG, and Upstage engineer native models with deep linguistic and contextual nuance.",
            "duration": "6:00 - 6:30"
        },
        {
            "num": 14,
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "The Shift from Frontier Monoliths to Domain-Specific sLLM & MoE",
            "subtitle": "Why Smaller, Specialized Models are Winning the Enterprise War",
            "bullets": [
                ("The Death of Monoliths", "1-Trillion parameter models are too slow and costly for private on-premises hosting."),
                ("Mixture-of-Experts (MoE)", "Activating only 20B-30B parameters out of 250B per token query."),
                ("Enterprise Advantages", "Deterministic latency (<50ms), lower compute overhead, and complete lifecycle ownership.")
            ],
            "visual": "Diagram contrasting Monolithic Dense Activation vs. Efficient Mixture-of-Experts (MoE) Routing.",
            "notes": "While public headlines celebrate trillion-parameter models, enterprise CFOs look at transaction costs. Domain sLLMs and MoE architectures deliver higher accuracy at a fraction of the cost.",
            "duration": "6:30 - 7:00"
        },
        {
            "num": 15,
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Cultural, Linguistic & Regulatory Alignment: The Sovereign Moat",
            "subtitle": "The Severe Cost of Cultural Hallucination in Corporate Workflows",
            "bullets": [
                ("Honorific Precision (Jondaetmal)", "Korean corporate communication requires exact contextual politeness."),
                ("Statutory Exactness", "Korean Commercial Code, labor laws, and tax regulations require precise citation."),
                ("Compliance Verification", "Sovereign models achieve 99.2% regulatory accuracy vs. ~71% for off-the-shelf global APIs.")
            ],
            "visual": "Side-by-side comparison of cultural and legal output accuracy: Global API vs. Sovereign Korean Model.",
            "notes": "In corporate Korea, an inappropriate honorific can jeopardize client relationships. Sovereign models are trained natively in Korean corporate etiquette and statutory legal codes.",
            "duration": "7:00 - 7:30"
        },
        {
            "num": 16,
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Model Optimization: INT4/NVFP4 Quantization & Pruning",
            "subtitle": "Compressing Frontier Models into Compact Workstation Footprints",
            "bullets": [
                ("Lossless Quantization", "Compressing FP16 weights down to INT4 and NVFP4 with under 1.5% perplexity loss."),
                ("Non-Uniform Pruning", "Surgically eliminating inactive attention heads tailored to specific enterprise domains."),
                ("Measurable Impact", "Memory footprint slashed by 70%, token generation increased from 18 to 65+ tokens/second.")
            ],
            "visual": "Performance graph showing throughput jump (tokens/sec) and VRAM reduction across INT4/FP16 formats.",
            "notes": "By applying INT4 and NVFP4 quantization, we shrink model memory requirements by 70% and triple throughput, allowing large models to run on affordable dual-GPU servers.",
            "duration": "7:30 - 8:00"
        },
        {
            "num": 17,
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Physical & Edge AI: Small Vision-Language-Action (VLA) Models",
            "subtitle": "Extending Sovereign Intelligence into Manufacturing and Smart Cities",
            "bullets": [
                ("SmolVLA & Compact Multimodal", "Enabling robotic arms and AGVs to interpret physical environments locally."),
                ("Intelligent Transport Systems (ITS)", "Nota.ai smart traffic edge controllers deployed across 200 intersections in Daejeon and Dubai RTA."),
                ("Zero Cloud Latency", "Real-time visual defect detection and signal optimization at 30 FPS.")
            ],
            "visual": "Case illustration: Edge AI controller in smart factory robotic arm and smart city intersection.",
            "notes": "Sovereign AI extends into the physical world. By embedding Small Vision-Language-Action models into edge hardware, we automate factory robotics and smart city traffic in real time.",
            "duration": "8:00 - 8:30"
        },
        {
            "num": 18,
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "The Enterprise Missing Link: Why 85% of AI PoCs Stall",
            "subtitle": "Bridging the Chasm Between Prototype Demos and Production Workflows",
            "bullets": [
                ("Hardware Mismatch", "Cloud-built prototypes fail when transitioned to corporate datacenter servers."),
                ("Data Silos", "Fragmented corporate data locked in legacy ERPs, internal PDFs, and legacy databases."),
                ("Security Void", "Absence of enterprise-grade hallucination guardrails, audit logging, and role-based access control.")
            ],
            "visual": "Pipeline diagram showing PoC failure points and MegazoneCloud's end-to-end bridge to production.",
            "notes": "85% of enterprise AI projects stall in prototype phase because integrating chips, models, databases, and compliance is overwhelming. That is the missing link MegazoneCloud resolves.",
            "duration": "8:30 - 9:00"
        },
        {
            "num": 19,
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "MegazoneCloud's 4-Layer Enterprise AI Full-Stack Architecture",
            "subtitle": "The Standardized, Modular Operating Blueprint for Enterprise AI",
            "image": os.path.join(img_dir, "slide19_solution_4layer_architecture.jpg"),
            "bullets": [
                ("Layer 4 (Applications)", "Air-Gapped RAG, AI Coding Agents, Executive Decision Portals."),
                ("Layer 3 (Model Serving)", "Nota NetsPresso optimization engine, vLLM, and Triton inference."),
                ("Layer 2 (Platform)", "Red Hat OpenShift AI (RHOAI) and Nutanix Cloud Infrastructure (NCI)."),
                ("Layer 1 (Hardware)", "Dell PowerEdge R760, NVIDIA H100 GPUs, and certified K-NPU servers.")
            ],
            "visual": "Detailed 4-Layer architectural diagram displaying software logos and interface protocols.",
            "notes": "Our 4-Layer Full-Stack architecture integrates certified hardware, virtualization, optimization compilers, and business applications into a single turnkey solution with one enterprise SLA.",
            "duration": "9:00 - 9:30"
        },
        {
            "num": 20,
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "Deep-Dive: From Nutanix/RHOAI (L2) to vLLM & Nota (L3)",
            "subtitle": "The Engine Room of Low-Latency, High-Density Model Serving",
            "bullets": [
                ("Layer 2 Virtualization", "Nutanix AHV and OpenShift AI automate GPU resource slicing (vGPU) across departments."),
                ("Layer 3 Compilation", "Nota NetsPresso profiles hardware and optimizes execution graphs automatically."),
                ("Continuous Batching", "vLLM PagedAttention ensures sub-second multi-tenant response times under high concurrency.")
            ],
            "visual": "Dataflow diagram tracing user query through Nutanix hypervisor to vLLM paged attention cache.",
            "notes": "At Layers 2 and 3, Nutanix and OpenShift virtualize GPU power across departments, while Nota and vLLM maximize inference density, extracting peak performance from minimum hardware.",
            "duration": "9:30 - 10:00"
        },
        {
            "num": 21,
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "Air-Gapped Security & Advanced Graph RAG (Mem0 + Graphify)",
            "subtitle": "True Data Moats: Zero Exfiltration Meets Deep Structural Context",
            "bullets": [
                ("100% Air-Gapped Isolation", "Zero external bytes transmitted; internal HSM key encryption."),
                ("Mem0 Memory Architecture", "Multi-session personalized context tracking user security clearance levels."),
                ("Graphify AST RAG", "Abstract Syntax Tree semantic parsing of enterprise source code and complex manuals.")
            ],
            "visual": "Security architecture diagram: Air-Gapped perimeter shield surrounding Mem0 context engine and Graph RAG.",
            "notes": "For banking and defense clients, we build completely air-gapped systems. Using Mem0 memory layers and Graphify knowledge graphs, our AI reasons across corporate manuals without hallucination.",
            "duration": "10:00 - 10:30"
        },
        {
            "num": 22,
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "The ISV Ecosystem: Orchestrating Global & Domestic Innovators",
            "subtitle": "The Power of the MegazoneCloud Multi-Vendor Aggregator Model",
            "bullets": [
                ("Global Category Leaders", "Articul8 (Autonomous GenAI) and Cohere (Multilingual Enterprise Embeddings)."),
                ("Domestic Specialist Champions", "Nota.ai (Edge Optimization), PuzzleData (Process Mining), QuantumAI (Air-Gapped AICC)."),
                ("Single Enterprise SLA", "Clients get multi-vendor best-of-breed software without contract chaos.")
            ],
            "visual": "Partner ecosystem wheel showing MegazoneCloud at center orchestrating global and domestic ISVs.",
            "notes": "We curate the world's finest ISVs. Whether bringing in Silicon Valley's Articul8 and Cohere or domestic champions like Nota and PuzzleData, we orchestrate them into one harmonious platform.",
            "duration": "10:30 - 11:00"
        },
        {
            "num": 23,
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Korea Inc. in Action: Enterprise AI Adoption Across Chaebols",
            "subtitle": "Real-World Deployments Across South Korea's Industrial Giants",
            "bullets": [
                ("Semiconductor & High-Tech", "Yield prediction, wafer defect inspection, and fab telemetry analytics."),
                ("Financial Services", "On-premise credit underwriting, automated compliance checks, and private analyst copilots."),
                ("Consumer Goods & Beauty (Amorepacific Context)", "Hyper-personalized beauty formulation compliant with PII laws."),
                ("Heavy Industry & Automotive", "Assembly line predictive maintenance and CAD engineering assistance.")
            ],
            "visual": "Industry mosaic illustrating live deployments across Manufacturing, Banking, Beauty, and Automotive.",
            "notes": "Pillar 4: Real enterprise adoption. In chip manufacturing, AI inspects wafers at line speed. In banking, private LLMs parse regulatory audits. In cosmetics, beauty algorithms run locally on customer data.",
            "duration": "11:00 - 11:30"
        },
        {
            "num": 24,
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Sovereign AI Turnkey Appliance: 1-Click On-Premises Deployment",
            "subtitle": "Delivering Enterprise AI as a Pre-Integrated, Plug-and-Play Appliance",
            "image": os.path.join(img_dir, "slide24_service_turnkey_appliance.jpg"),
            "bullets": [
                ("Pre-Integrated Hardware", "Pre-racked Dell R760 2U server with certified NVIDIA GPUs or K-NPUs."),
                ("Rapid Time-to-Value", "From power-on to first internal query in under 2 hours (vs. 6 months of consulting)."),
                ("Built-In Governance", "Pre-loaded with Nutanix AHV, Nota NetsPresso INT4, and sovereign domain models.")
            ],
            "visual": "Product rendering of the 2U rack appliance showing pre-installed software layers and plug-in setup.",
            "notes": "We package sovereign AI into a plug-and-play 2U appliance. Arrives pre-tested; you connect power and ethernet, and your company has an air-gapped private intelligence platform running in 2 hours.",
            "duration": "11:30 - 12:00"
        },
        {
            "num": 25,
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Measurable Business ROI: 75% Capex Cut & 3.2kW Power Feasibility",
            "subtitle": "The Hard Financial and Operational Metrics of Success",
            "bullets": [
                ("Capex Slashed by 75%", "$120,000 USD dual-GPU appliance replaces standard $480,000 USD 8-GPU cluster."),
                ("Power Draw at 3.2kW", "Safely fits standard 10kW datacenter racks, eliminating costly room retrofits."),
                ("Latency Reduced 3x", "Deterministic sub-50ms token generation for seamless user experience."),
                ("Zero Data Exfiltration", "100% compliance with strict national banking and defense security mandates.")
            ],
            "visual": "Executive ROI scorecard with side-by-side metric tables and large callout badges (75% SAVINGS).",
            "notes": "These are the metrics that win boardroom approval: 75% Capex savings, 3.2kW power consumption that avoids facility reconstruction, and sub-50ms latency with zero data leakage.",
            "duration": "12:00 - 12:30"
        },
        {
            "num": 26,
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Public Sector & 'AI for All Citizens': National Transformation",
            "subtitle": "Democratizing Artificial Intelligence Across Civil Administration and Healthcare",
            "bullets": [
                ("AI Civil Servants", "Automating routine civic administration, tax filings, and municipal inquiries."),
                ("Universal AI Compute Vouchers", "Subsidizing AI compute for 10,000+ domestic SMEs and technology startups."),
                ("Healthcare & Rural Equity", "Deploying sovereign diagnostic assistants to regional clinics to bridge medical gaps.")
            ],
            "visual": "Infographic showing government civic portal, regional hospital diagnostic network, and SME grant flow.",
            "notes": "Sovereign AI is also a public good. Korea's 'AI for All' initiative delivers AI assistants to municipal offices and regional clinics, ensuring technological advancement benefits all citizens.",
            "duration": "12:30 - 13:00"
        },
        {
            "num": 27,
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "MegazoneCloud's Growth Story: From Cloud Pioneer to AI Unicorn",
            "subtitle": "The Operational Architect Behind Korea's Digital Infrastructure",
            "bullets": [
                ("1998 to Present", "Early digital agency evolved into Korea's first AWS Premier Consulting Partner in 2012."),
                ("Official Unicorn (2022)", "Valuation exceeded $1.8B USD, leading the Korean cloud MSP market."),
                ("Scale Today", "Over 2,700 enterprise clients, 1,500+ specialized engineers, and multi-cloud market dominance."),
                ("The Strategic Evolution", "Cloud MSP -> AI MSP -> Global Full-Stack Sovereign AI Orchestrator.")
            ],
            "visual": "Milestone timeline spanning 1998, 2012, 2022, and 2026 showing revenue and client expansion trajectory.",
            "notes": "MegazoneCloud pioneered cloud computing in Korea over a decade ago as the country's first AWS Premier Partner. Today, as a multi-billion dollar tech unicorn, we are leading the AI transformation wave.",
            "duration": "13:00 - 13:30"
        },
        {
            "num": 28,
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Global Expansion Playbook: Bridging Korea, US, Japan & SE Asia",
            "subtitle": "Exporting Sovereign AI Methodologies to High-Growth Asian Markets",
            "image": os.path.join(img_dir, "slide28_mzc_global_ai_bridge.jpg"),
            "bullets": [
                ("Silicon Valley Hub (Palo Alto)", "Venture partnerships, co-innovation with frontier AI ISVs."),
                ("Japan Expansion (Tokyo)", "Delivering sovereign on-premise AI to Japanese financial and enterprise leaders."),
                ("Southeast Asia (Singapore, Vietnam)", "Scaling low-power NPU inference appliances and cloud software."),
                ("The Strategic Bridge", "Connecting Western software innovation with Asian enterprise operational execution.")
            ],
            "visual": "Global map linking Silicon Valley, Seoul, Tokyo, and Singapore with active business flows.",
            "notes": "We are expanding globally. Through offices in Palo Alto, Tokyo, and Singapore, we export the sovereign AI methodologies proven in Korea to enterprises across the Asia-Pacific region.",
            "duration": "13:30 - 14:00"
        },
        {
            "num": 29,
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Strategic Takeaways for Global Business Leaders",
            "subtitle": "Key Insights for UCLA Anderson Executive MBA Delegates",
            "bullets": [
                ("1. Sovereignty != Isolation", "True strategic autonomy combines global technological standards with local control."),
                ("2. Datacenter Physics Rule", "Power, rack limits, and thermal constraints dictate AI feasibility faster than ambition."),
                ("3. Defend Your Proprietary Moat", "Internal domain knowledge and proprietary data graphs are your core balance sheet assets."),
                ("4. Modular Architectural Agility", "Decouple silicon, foundation models, and middleware to prevent future vendor lock-in.")
            ],
            "visual": "4 quadrant strategic framework summarizing executive recommendations for global leaders.",
            "notes": "As you return to your executive roles, remember: true sovereignty is about agility, not isolation. Respect datacenter physics early, guard your corporate data, and build modular systems.",
            "duration": "14:00 - 14:30"
        },
        {
            "num": 30,
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Conclusion & Open Q&A Discussion",
            "subtitle": "Shaping the Future of Enterprise AI Together",
            "bullets": [
                ("Presenter", "Andy | ISV Business Unit & AI Architecture Group, MegazoneCloud"),
                ("Official Email", "andy@megazone.com | contact@megazone.com"),
                ("Headquarters", "MegazoneCloud Gwacheon Smart Tower, Gwacheon-si, Gyeonggi-do, Korea"),
                ("Open Floor Discussion", "Comparative regulatory policies, NPU vs. GPU economics, scaling across global subsidiaries.")
            ],
            "visual": "Collaborative closing slide with MegazoneCloud and UCLA Anderson logos and live Q&A floor open banner.",
            "notes": "Thank you for your time, leadership, and attention. The future of AI will be shaped by strategic autonomy and global collaboration. The floor is now open for your questions.",
            "duration": "14:30 - 15:00"
        }
    ]

    blank_layout = prs.slide_layouts[6]

    # 슬라이드 생성 루프
    for s_idx, s in enumerate(slides_data):
        slide = prs.slides.add_slide(blank_layout)

        # 1. 배경 설정 (Cover vs 일반 슬라이드)
        is_cover = (s["num"] == 1)

        if is_cover:
            # 커버 슬라이드 배경 (다크 네이비 그라데이션 박스)
            bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = COLOR_NAVY_DARK
            bg_shape.line.fill.background()

            # 상단 배지 (UCLA Gold)
            badge_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(6.5), Inches(0.45))
            badge_box.fill.solid()
            badge_box.fill.fore_color.rgb = COLOR_NAVY_MED
            badge_box.line.color.rgb = COLOR_GOLD
            tf_b = badge_box.text_frame
            tf_b.word_wrap = True
            p_b = tf_b.paragraphs[0]
            p_b.alignment = PP_ALIGN.CENTER
            r_b = p_b.add_run()
            r_b.text = "UCLA ANDERSON EXECUTIVE MBA DELEGATION VISIT | SEOUL 2026"
            r_b.font.size = Pt(11)
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_GOLD

            # 메인 타이틀 박스
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(7.5), Inches(2.2))
            tf_t = title_box.text_frame
            tf_t.word_wrap = True
            p_t = tf_t.paragraphs[0]
            r_t = p_t.add_run()
            r_t.text = s["title"]
            r_t.font.name = "Arial"
            r_t.font.size = Pt(32)
            r_t.font.bold = True
            r_t.font.color.rgb = COLOR_WHITE

            # 서브타이틀
            p_sub = tf_t.add_paragraph()
            p_sub.space_before = Pt(12)
            r_sub = p_sub.add_run()
            r_sub.text = s["subtitle"]
            r_sub.font.name = "Arial"
            r_sub.font.size = Pt(15)
            r_sub.font.color.rgb = COLOR_MZC_CYAN

            # 발표자 정보 박스
            info_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(7.2), Inches(2.2))
            info_box.fill.solid()
            info_box.fill.fore_color.rgb = RGBColor(14, 23, 38)
            info_box.line.color.rgb = RGBColor(0, 102, 255)
            tf_info = info_box.text_frame
            tf_info.word_wrap = True
            
            p_i1 = tf_info.paragraphs[0]
            r_i1_h = p_i1.add_run()
            r_i1_h.text = "Session: "
            r_i1_h.font.bold = True
            r_i1_h.font.size = Pt(12)
            r_i1_h.font.color.rgb = COLOR_GOLD
            r_i1_t = p_i1.add_run()
            r_i1_t.text = "Session 3 - Korea Sovereign AI Strategy (English Presentation)"
            r_i1_t.font.size = Pt(12)
            r_i1_t.font.color.rgb = COLOR_WHITE

            p_i2 = tf_info.add_paragraph()
            p_i2.space_before = Pt(6)
            r_i2_h = p_i2.add_run()
            r_i2_h.text = "Speaker: "
            r_i2_h.font.bold = True
            r_i2_h.font.size = Pt(12)
            r_i2_h.font.color.rgb = COLOR_GOLD
            r_i2_t = p_i2.add_run()
            r_i2_t.text = "Andy | ISV Business Unit & AI Architecture Group, MegazoneCloud"
            r_i2_t.font.size = Pt(12)
            r_i2_t.font.color.rgb = COLOR_WHITE

            p_i3 = tf_info.add_paragraph()
            p_i3.space_before = Pt(6)
            r_i3_h = p_i3.add_run()
            r_i3_h.text = "Date & Venue: "
            r_i3_h.font.bold = True
            r_i3_h.font.size = Pt(11)
            r_i3_h.font.color.rgb = COLOR_TEXT_MUTED
            r_i3_t = p_i3.add_run()
            r_i3_t.text = "Friday, September 11, 2026 | MegazoneCloud Gwacheon HQ (2F Grand Room)"
            r_i3_t.font.size = Pt(11)
            r_i3_t.font.color.rgb = COLOR_TEXT_MUTED

            # 커버 우측 이미지
            if "image" in s and os.path.exists(s["image"]):
                img_left = Inches(8.3)
                img_top = Inches(1.5)
                img_w = Inches(4.3)
                img_h = Inches(5.0)
                slide.shapes.add_picture(s["image"], img_left, img_top, width=img_w, height=img_h)

        else:
            # 일반 내지 슬라이드 (화이트/라이트 그레이 배경 + 상단 헤더 바)
            bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = COLOR_CARD_BG
            bg_shape.line.fill.background()

            # 상단 헤더 배경 띠
            header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.3))
            header_bar.fill.solid()
            header_bar.fill.fore_color.rgb = COLOR_WHITE
            header_bar.line.color.rgb = COLOR_CARD_BORDER

            # 좌측 상단: 슬라이드 제목
            title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.12), Inches(9.5), Inches(0.65))
            tf_t = title_box.text_frame
            tf_t.word_wrap = True
            p_t = tf_t.paragraphs[0]
            r_t = p_t.add_run()
            r_t.text = f"{s['num']}.  {s['title']}"
            r_t.font.name = "Arial"
            r_t.font.size = Pt(21)
            r_t.font.bold = True
            r_t.font.color.rgb = COLOR_NAVY_DARK

            # 상단 소제목 (Key Theme)
            sub_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.75), Inches(9.5), Inches(0.45))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            r_sub = p_sub.add_run()
            r_sub.text = s["subtitle"]
            r_sub.font.name = "Arial"
            r_sub.font.size = Pt(12)
            r_sub.font.color.rgb = COLOR_MZC_BLUE
            r_sub.font.bold = True

            # 우측 상단 파트 배지
            part_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(0.35), Inches(2.8), Inches(0.42))
            part_badge.fill.solid()
            part_badge.fill.fore_color.rgb = COLOR_NAVY_MED
            part_badge.line.color.rgb = COLOR_GOLD
            tf_pb = part_badge.text_frame
            tf_pb.word_wrap = True
            p_pb = tf_pb.paragraphs[0]
            p_pb.alignment = PP_ALIGN.CENTER
            r_pb = p_pb.add_run()
            r_pb.text = s["part"]
            r_pb.font.size = Pt(9.5)
            r_pb.font.bold = True
            r_pb.font.color.rgb = COLOR_GOLD

            has_image = ("image" in s and os.path.exists(s["image"]))

            if has_image:
                # 2열 분할 레이아웃 (좌측 불릿 6.8인치, 우측 이미지 5.1인치)
                bullet_left = Inches(0.7)
                bullet_width = Inches(6.8)
                img_left = Inches(7.7)
                img_top = Inches(1.5)
                img_width = Inches(4.9)
                img_height = Inches(4.8)

                # 우측 이미지 배치
                slide.shapes.add_picture(s["image"], img_left, img_top, width=img_width, height=img_height)

                # 좌측 불릿 카드 3개
                card_y = Inches(1.5)
                card_h = Inches(1.45)
                card_gap = Inches(0.18)

                for b_idx, (headline, body) in enumerate(s["bullets"]):
                    cur_y = card_y + b_idx * (card_h + card_gap)
                    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bullet_left, cur_y, bullet_width, card_h)
                    card.fill.solid()
                    card.fill.fore_color.rgb = COLOR_WHITE
                    card.line.color.rgb = COLOR_CARD_BORDER
                    
                    # 좌측 세로 컬러 포인트 바
                    p_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bullet_left, cur_y, Inches(0.1), card_h)
                    p_bar.fill.solid()
                    p_bar.fill.fore_color.rgb = COLOR_MZC_BLUE if b_idx % 2 == 0 else COLOR_MZC_CYAN
                    p_bar.line.fill.background()

                    tf_c = card.text_frame
                    tf_c.word_wrap = True
                    tf_c.margin_left = Inches(0.3)
                    tf_c.margin_right = Inches(0.2)
                    tf_c.margin_top = Inches(0.15)
                    tf_c.margin_bottom = Inches(0.1)

                    p_head = tf_c.paragraphs[0]
                    r_dot = p_head.add_run()
                    r_dot.text = f"{b_idx + 1}.  "
                    r_dot.font.bold = True
                    r_dot.font.size = Pt(12)
                    r_dot.font.color.rgb = COLOR_MZC_BLUE

                    r_head = p_head.add_run()
                    r_head.text = headline
                    r_head.font.bold = True
                    r_head.font.size = Pt(12)
                    r_head.font.color.rgb = COLOR_NAVY_DARK

                    p_body = tf_c.add_paragraph()
                    p_body.space_before = Pt(3)
                    r_body = p_body.add_run()
                    r_body.text = body
                    r_body.font.size = Pt(10)
                    r_body.font.color.rgb = COLOR_TEXT_MAIN

            else:
                # 전체 너비 불릿 카드 레이아웃 (카드 너비 11.9인치)
                card_left = Inches(0.7)
                card_width = Inches(11.9)
                card_y = Inches(1.55)
                
                num_bullets = len(s["bullets"])
                card_h = Inches(1.15) if num_bullets >= 4 else Inches(1.4)
                card_gap = Inches(0.16)

                for b_idx, (headline, body) in enumerate(s["bullets"]):
                    cur_y = card_y + b_idx * (card_h + card_gap)
                    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_left, cur_y, card_width, card_h)
                    card.fill.solid()
                    card.fill.fore_color.rgb = COLOR_WHITE
                    card.line.color.rgb = COLOR_CARD_BORDER

                    # 좌측 세로 컬러 포인트 바
                    p_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, card_left, cur_y, Inches(0.12), card_h)
                    p_bar.fill.solid()
                    p_bar.fill.fore_color.rgb = COLOR_MZC_BLUE if b_idx % 2 == 0 else COLOR_MZC_CYAN
                    p_bar.line.fill.background()

                    tf_c = card.text_frame
                    tf_c.word_wrap = True
                    tf_c.margin_left = Inches(0.35)
                    tf_c.margin_right = Inches(0.25)
                    tf_c.margin_top = Inches(0.12)

                    p_head = tf_c.paragraphs[0]
                    r_dot = p_head.add_run()
                    r_dot.text = f"{b_idx + 1}.  "
                    r_dot.font.bold = True
                    r_dot.font.size = Pt(13)
                    r_dot.font.color.rgb = COLOR_MZC_BLUE

                    r_head = p_head.add_run()
                    r_head.text = headline
                    r_head.font.bold = True
                    r_head.font.size = Pt(13)
                    r_head.font.color.rgb = COLOR_NAVY_DARK

                    p_body = tf_c.add_paragraph()
                    p_body.space_before = Pt(3)
                    r_body = p_body.add_run()
                    r_body.text = body
                    r_body.font.size = Pt(11)
                    r_body.font.color.rgb = COLOR_TEXT_MAIN

            # 하단 비주얼 캡션 바
            v_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(6.5), Inches(11.9), Inches(0.35))
            v_bar.fill.solid()
            v_bar.fill.fore_color.rgb = RGBColor(238, 242, 246)
            v_bar.line.fill.background()
            tf_v = v_bar.text_frame
            p_v = tf_v.paragraphs[0]
            p_v.alignment = PP_ALIGN.LEFT
            tf_v.margin_left = Inches(0.15)
            r_vl = p_v.add_run()
            r_vl.text = "VISUAL CONCEPT: "
            r_vl.font.bold = True
            r_vl.font.size = Pt(9)
            r_vl.font.color.rgb = COLOR_NAVY_MED
            r_vt = p_v.add_run()
            r_vt.text = s["visual"]
            r_vt.font.italic = True
            r_vt.font.size = Pt(9)
            r_vt.font.color.rgb = COLOR_TEXT_MUTED

            # 하단 푸터 라인 & 텍스트
            footer_text = slide.shapes.add_textbox(Inches(0.7), Inches(6.95), Inches(10.0), Inches(0.35))
            tf_f = footer_text.text_frame
            p_f = tf_f.paragraphs[0]
            r_f = p_f.add_run()
            r_f.text = "UCLA Anderson Executive MBA Delegation Visit | Session 3: Korea Sovereign AI Strategy | Speaker: Andy"
            r_f.font.size = Pt(9)
            r_f.font.color.rgb = COLOR_TEXT_MUTED

            page_num_box = slide.shapes.add_textbox(Inches(11.0), Inches(6.95), Inches(1.6), Inches(0.35))
            tf_pn = page_num_box.text_frame
            p_pn = tf_pn.paragraphs[0]
            p_pn.alignment = PP_ALIGN.RIGHT
            r_pn = p_pn.add_run()
            r_pn.text = f"{s['num']} / 30"
            r_pn.font.size = Pt(10)
            r_pn.font.bold = True
            r_pn.font.color.rgb = COLOR_NAVY_MED

        # 3. 스피커 대본(Speaker Notes) 삽입
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        tf_notes.text = f"[PACING: {s['duration']}]\n\n{s['notes']}"

    # 최종 저장
    prs.save(output_path)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Successfully created 30-Slide Sovereign AI Deck: {output_path} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    build_sovereign_ai_pptx()
