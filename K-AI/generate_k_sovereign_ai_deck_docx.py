# -*- coding: utf-8 -*-
"""
UCLA Anderson Executive MBA 내방 세션용 Sovereign AI 전략 30슬라이드 공식 Word(DOCX) 생성기
- 작성일자: 2026-09-09
- 대상: UCLA Anderson EMBA 방문단 (50명)
- 발표자: Andy (ISV Business Unit & AI Architecture Group, MegazoneCloud)
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """표 셀의 배경색을 지정하는 헬퍼 함수"""
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """표 셀의 내부 여백을 설정하는 헬퍼 함수"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for margin_name, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{margin_name}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_sovereign_ai_deck_docx():
    doc = Document()

    # 페이지 여백 설정 (A4, 1인치 여백)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # 1. 문서 메인 타이틀 & 행사 정보 블록
    title_table = doc.add_table(rows=1, cols=1)
    title_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    title_cell = title_table.cell(0, 0)
    set_cell_background(title_cell, "002B49")  # UCLA Deep Navy
    set_cell_margins(title_cell, top=280, bottom=280, left=280, right=280)

    p_badge = title_cell.paragraphs[0]
    p_badge.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_badge = p_badge.add_run("UCLA ANDERSON EXECUTIVE MBA DELEGATION VISIT | SEOUL 2026")
    run_badge.font.name = "Arial"
    run_badge.font.size = Pt(10)
    run_badge.font.bold = True
    run_badge.font.color.rgb = RGBColor(255, 209, 0)  # UCLA Gold

    p_title = title_cell.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("Korea's Sovereign AI Strategy: From Silicon to Enterprise Applications")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(255, 255, 255)

    p_sub = title_cell.add_paragraph()
    run_sub = p_sub.add_run("30-Slide Executive Presentation Deck & Speaker Delivery Guide")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = RGBColor(200, 220, 245)

    # 메타데이터 표
    doc.add_paragraph().paragraph_format.space_before = Pt(8)
    meta_table = doc.add_table(rows=2, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        [("Date & Time", "Friday, September 11, 2026 | 10:00 - 11:30 AM KST"), ("Venue", "MegazoneCloud Gwacheon HQ, 2F Grand Conference Room")],
        [("Target Audience", "UCLA Anderson EMBA (44 Executives + 6 Faculty/Staff)"), ("Speaker & Unit", "Andy | ISV Business Unit & AI Architecture Group")]
    ]
    for r_idx, row in enumerate(meta_data):
        for c_idx, (k, v) in enumerate(row):
            cell = meta_table.cell(r_idx, c_idx)
            set_cell_background(cell, "F4F7FB" if (r_idx+c_idx)%2==0 else "E9EEF5")
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            p = cell.paragraphs[0]
            r_k = p.add_run(f"{k}: ")
            r_k.font.bold = True
            r_k.font.size = Pt(9.5)
            r_k.font.color.rgb = RGBColor(0, 59, 92)
            r_v = p.add_run(v)
            r_v.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 슬라이드 데이터 30개 정의
    slides = [
        {
            "num": "01",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "Title & Welcome: Korea Sovereign AI Strategy",
            "subtitle": "Unlocking Strategic Autonomy, Native Infrastructure, and Scalable Transformation",
            "bullets": [
                "Welcome to MegazoneCloud Gwacheon HQ for the UCLA Anderson EMBA Seoul Immersion.",
                "South Korea is one of only three countries with an end-to-end native AI full stack.",
                "Bridging world-class semiconductor hardware (NPU/HBM) with enterprise sovereign software."
            ],
            "visual": "Futuristic visual blending Seoul skyline, AI neural nodes, and enterprise server racks.",
            "notes": "Good morning, faculty and executives of UCLA Anderson EMBA. On behalf of MegazoneCloud, welcome to our Gwacheon HQ. Today, we present South Korea's sovereign AI playbook—from silicon to enterprise software.",
            "duration": "0:00 - 0:30"
        },
        {
            "num": "02",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "Welcome UCLA Anderson EMBA: Objectives & Agenda",
            "subtitle": "Today's 15-Minute Executive Briefing & Collaborative Exchange",
            "bullets": [
                "Understanding the geopolitical, financial, and technical drivers behind Sovereign AI.",
                "The 4-Pillar Strategic Framework: Infrastructure -> Model -> Solution -> Service.",
                "MegazoneCloud's playbook: Scaling from Korea's #1 Cloud Unicorn to global AI orchestrator.",
                "Contextualizing with your Seoul visits: Samsung, DEEPX, Amorepacific, and Invest Seoul."
            ],
            "visual": "Flow diagram showing 3-stage presentation breakdown and interactive Q&A roadmap.",
            "notes": "Over the next 15 minutes, we will unpack why sovereign AI is an urgent commercial reality and how Korea provides an actionable template for global enterprise leaders.",
            "duration": "0:30 - 1:00"
        },
        {
            "num": "03",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The Geopolitics of AI: Why 'Sovereignty' Matters in 2026",
            "subtitle": "From AI Experimentation to Strategic Operational Autonomy",
            "bullets": [
                "The AI Duopoly Threat: Over-reliance on foreign hyperscalers exposes firms to price spikes, outage risks, and lock-in.",
                "Sovereign AI 2.0 Defined: 'Operational Sovereignty' and 'Access Autonomy'—ensuring mission-critical systems run offline.",
                "Regulatory Compliance: Stringent data residency laws (EU AI Act, Korea PIPA, Financial Cloud Directives)."
            ],
            "visual": "Comparison matrix: Cloud SaaS API Risks vs. Air-Gapped Sovereign AI Enterprise Benefits.",
            "notes": "In 2026, the question is no longer 'Which API is smartest?' but 'Who owns our intelligence? If cross-border connections drop, can our business still operate?'",
            "duration": "1:00 - 1:30"
        },
        {
            "num": "04",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "South Korea's Unique Position: The World's 3rd AI Powerhouse",
            "subtitle": "A Rare Convergence of Semiconductor, Software, and Heavy Industry",
            "bullets": [
                "Elite Global Trio: Only US, China, and South Korea possess complete end-to-end AI capabilities.",
                "Hardware Dominance: World's leading memory/HBM manufacturing (Samsung Electronics, SK Hynix).",
                "Digital Platforms & Models: Domestic tech giants (Naver, Kakao) beating global platforms locally.",
                "The 'G3 Ambition': Formal government roadmap to become a Global Top 3 AI Powerhouse by 2027."
            ],
            "visual": "Global map highlighting US, China, and Korea with 4-layer full-stack capability indicators.",
            "notes": "Korea possesses the entire physical and digital vertical stack. We build the memory chips, host native search engines, and manufacture ships, cars, and consumer electronics.",
            "duration": "1:30 - 2:00"
        },
        {
            "num": "05",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The Enterprise Trilemma: Capex, Power, and Data Sovereignty",
            "subtitle": "The Hard Physical Bottlenecks Stalling On-Premises Deployments",
            "bullets": [
                "Financial Shock (Capex): 8-GPU servers cost $400K-$500K each with unpredictable delivery cycles.",
                "Physical Power Cap: 90% of corporate datacenter racks are limited to 8-10kW; 8-GPU servers draw 10.2kW.",
                "Data Exfiltration Risk: Defense, banking, and semiconductor fabs strictly forbid transmitting IP to public clouds."
            ],
            "visual": "Trilemma diagram: High Capex vs. 10kW Rack Power Limit vs. Air-Gapped Security Requirements.",
            "notes": "When enterprise CTOs attempt to run 250B parameter models on-premises, they hit an electrical brick wall. Overcoming this physical trilemma is our primary engineering focus.",
            "duration": "2:00 - 2:30"
        },
        {
            "num": "06",
            "part": "PART 1: MACRO CONTEXT & IMPERATIVE",
            "title": "The 4-Pillar Framework: Infra, Model, Solution, Service",
            "subtitle": "The Unified Architecture of National & Enterprise AI Independence",
            "bullets": [
                "Pillar 1 (Infrastructure): Compute clusters, public AI highway, and native NPU semiconductors.",
                "Pillar 2 (Model): Sovereign Korean foundation models, domain sLLMs, and Mixture-of-Experts (MoE).",
                "Pillar 3 (Solution): Full-stack orchestration, air-gapped security, and model optimization compilers.",
                "Pillar 4 (Service): Cross-industry deployment across Chaebols, SMEs, and public administrative sectors."
            ],
            "visual": "4-Layer architectural pyramid highlighting synchronized execution across government and private sector.",
            "notes": "Sovereignty fails if any single layer is missing. Korea's strategy coordinates all 4 pillars synchronously to deliver commercial and operational success.",
            "duration": "2:30 - 3:00"
        },
        {
            "num": "07",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "National AI Computing Center: The Public-Private 'AI Highway'",
            "subtitle": "A Multi-Billion Dollar Sovereign Compute Megaproject",
            "bullets": [
                "Solaseado Datacenter Park: Broken ground in August 2026 in Haenam, South Jeolla Province.",
                "Public-Private Consortium: Led by MSIT and Samsung SDS via a dedicated Special Purpose Company (SPC).",
                "National Compute Bedrock: Subsidizing massive compute access for universities, startups, and domestic industry."
            ],
            "visual": "Architectural rendering of Haenam Solaseado datacenter campus with green energy grid connections.",
            "notes": "Pillar 1 begins with compute. In August 2026, Korea broke ground on the National AI Computing Center in Haenam, ensuring domestic industry is protected from international GPU supply crunches.",
            "duration": "3:00 - 3:30"
        },
        {
            "num": "08",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Compute Capacity Scaling: 15,000 GPUs to 50,000 GPUs",
            "subtitle": "The Exponential Trajectory of Public Compute Infrastructure",
            "bullets": [
                "Phase 1 (2026 - 2028): Initial deployment of 15,000 top-tier AI accelerators (H100/B200 tier).",
                "Phase 2 (2029 - 2030+): Expansion to 50,000+ accelerators integrated with coastal offshore wind power.",
                "Sovereign Resource Allocation: Tiered vouchers enabling rapid model training without predatory cloud pricing."
            ],
            "visual": "Growth chart showing GPU capacity scaling from 15K to 50K units by 2030 with power efficiency curves.",
            "notes": "Reaching 15,000 accelerators by 2028 and 50,000 by 2030 establishes a fortress of compute capacity that underpins national digital sovereignty.",
            "duration": "3:30 - 4:00"
        },
        {
            "num": "09",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "The Rise of K-NPU: The 'K-Cloud' Initiative & NPU Farms",
            "subtitle": "Disrupting the AI Inference Landscape with High-Efficiency Silicon",
            "bullets": [
                "K-Cloud Initiative: Over $600M in national backing to develop ultra-low-power AI semiconductors.",
                "The 80/20 Rule: While model training requires GPUs, over 80% of operational enterprise TCO is inference.",
                "NPU Farms in Action: Live multi-petaflop clusters deployed across Naver, KT, and NHN Cloud datacenters."
            ],
            "visual": "Inference TCO comparison: K-NPU vs. Traditional GPU showing power and cost savings.",
            "notes": "Up to 80% of enterprise AI costs are inference. Korea's K-Cloud project deploys native NPUs specifically engineered to execute inference at a fraction of standard GPU power.",
            "duration": "4:00 - 4:30"
        },
        {
            "num": "10",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Korea's Fabless Champions: Rebellions, FuriosaAI, DEEPX, Mobilint",
            "subtitle": "Purpose-Built Silicon Across Datacenter, Edge, and Robotics",
            "bullets": [
                "Rebellions (ATOM / ATOM-MAX): High-throughput datacenter inference and financial algorithmic trading.",
                "FuriosaAI (WARBOY / RENEGADE): High-efficiency computer vision and Transformer model acceleration.",
                "DEEPX (All-in-4 AI Series): Ultra-low-power on-device NPU for smart mobility, IoT, and industrial robotics (On UCLA Itinerary!).",
                "Mobilint (ARIES / REGULUS): Edge AI solutions for industrial automation."
            ],
            "visual": "Silicon ecosystem landscape mapping Korean fabless startups across Datacenter, Edge, and On-Device tiers.",
            "notes": "Many of you are visiting DEEPX this week. DEEPX, Rebellions, and FuriosaAI are not mimicking GPUs; they are building purpose-driven architectures that win on efficiency.",
            "duration": "4:30 - 5:00"
        },
        {
            "num": "11",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Enterprise Hybrid Cloud & GPUaaS: Dell, NVIDIA, and Akamai",
            "subtitle": "Balancing Tier-1 Global Standards with Modular Sovereign Clouds",
            "bullets": [
                "Mainstream Enterprise Track: Dell PowerEdge R760 + NVIDIA GPUs for on-premise high performance.",
                "Cost-Optimized GPUaaS: Partnership with Akamai Distributed Cloud for sub-millisecond edge inferencing at 40% lower egress.",
                "Hybrid Topology: Sensitive proprietary IP kept strictly on-premises; public workloads burst to sovereign cloud."
            ],
            "visual": "Hybrid network architecture showing Dell On-Premises core connected to Akamai GPUaaS edge nodes.",
            "notes": "Sovereignty is not isolation. MegazoneCloud delivers certified Dell and NVIDIA enterprise stacks while leveraging distributed GPUaaS partnerships like Akamai to optimize client TCO.",
            "duration": "5:00 - 5:30"
        },
        {
            "num": "12",
            "part": "PART 2: PILLAR 1 - INFRASTRUCTURE & SILICON",
            "title": "Overcoming Data Center Bottlenecks: 10kW Rack Power & Cooling",
            "subtitle": "Engineering Feasibility in Existing Corporate Server Rooms",
            "bullets": [
                "The Datacenter Bottleneck: Retrofitting legacy server rooms with liquid cooling costs millions and causes downtime.",
                "Dense 2-GPU Form Factor: High-efficiency 2U dual-GPU architecture delivering enterprise-grade throughput.",
                "Power Feasibility: Operating power capped at 3.2kW, safely within standard 10kW datacenter rack limits."
            ],
            "visual": "Server rack diagram showing 3.2kW 2-GPU server fitting comfortably into standard 10kW rack space.",
            "notes": "Our dual-GPU dense form factor caps power draw at 3.2kW. Enterprises can deploy sovereign AI in their existing server rooms tomorrow without electrical rewiring.",
            "duration": "5:30 - 6:00"
        },
        {
            "num": "13",
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Korea's Foundation Model Landscape",
            "subtitle": "Native Linguistic Mastery and Frontier Enterprise Intelligence",
            "bullets": [
                "Naver HyperCLOVA X: Dominant commercial hyper-scale model trained on 6,500x more Korean data than GPT-3.",
                "LG AI Research EXAONE 3.0: High-performance bilingual open-weight model engineered for chemistry, patents, and manufacturing.",
                "Upstage Solar: Globally acclaimed sLLM leading HuggingFace benchmarks via innovative Depth-Up Scaling (DUS)."
            ],
            "visual": "Logo and performance matrix comparing HyperCLOVA X, EXAONE 3.0, and Solar across enterprise benchmarks.",
            "notes": "Pillar 2: Models. Korea does not rely solely on translated foreign LLMs. Naver, LG, and Upstage engineer native models with deep linguistic and contextual nuance.",
            "duration": "6:00 - 6:30"
        },
        {
            "num": "14",
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "The Shift from Frontier Monoliths to Domain-Specific sLLM & MoE",
            "subtitle": "Why Smaller, Specialized Models are Winning the Enterprise War",
            "bullets": [
                "The Death of Monoliths: 1-Trillion parameter models are too slow and costly for private on-premises hosting.",
                "Mixture-of-Experts (MoE): Activating only 20B-30B parameters out of 250B per token query.",
                "Enterprise Advantages: Deterministic latency (<50ms), lower compute overhead, and complete lifecycle ownership."
            ],
            "visual": "Diagram contrasting Monolithic Dense Activation vs. Efficient Mixture-of-Experts (MoE) Routing.",
            "notes": "While public headlines celebrate trillion-parameter models, enterprise CFOs look at transaction costs. Domain sLLMs and MoE architectures deliver higher accuracy at a fraction of the cost.",
            "duration": "6:30 - 7:00"
        },
        {
            "num": "15",
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Cultural, Linguistic & Regulatory Alignment: The Sovereign Moat",
            "subtitle": "The Severe Cost of Cultural Hallucination in Corporate Workflows",
            "bullets": [
                "Honorific Precision (Jondaetmal): Korean corporate communication requires exact contextual politeness.",
                "Statutory Exactness: Korean Commercial Code, labor laws, and tax regulations require precise citation.",
                "Compliance Verification: Sovereign models achieve 99.2% regulatory accuracy vs. ~71% for off-the-shelf global APIs."
            ],
            "visual": "Side-by-side comparison of cultural and legal output accuracy: Global API vs. Sovereign Korean Model.",
            "notes": "In corporate Korea, an inappropriate honorific can jeopardize client relationships. Sovereign models are trained natively in Korean corporate etiquette and statutory legal codes.",
            "duration": "7:00 - 7:30"
        },
        {
            "num": "16",
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Model Optimization: INT4/NVFP4 Quantization & Pruning",
            "subtitle": "Compressing Frontier Models into Compact Workstation Footprints",
            "bullets": [
                "Lossless Quantization: Compressing FP16 weights down to INT4 and NVFP4 with under 1.5% perplexity loss.",
                "Non-Uniform Pruning: Surgically eliminating inactive attention heads tailored to specific enterprise domains.",
                "Measurable Impact: Memory footprint slashed by 70%, token generation increased from 18 to 65+ tokens/second."
            ],
            "visual": "Performance graph showing throughput jump (tokens/sec) and VRAM reduction across INT4/FP16 formats.",
            "notes": "By applying INT4 and NVFP4 quantization, we shrink model memory requirements by 70% and triple throughput, allowing large models to run on affordable dual-GPU servers.",
            "duration": "7:30 - 8:00"
        },
        {
            "num": "17",
            "part": "PART 3: PILLAR 2 - FOUNDATION MODELS",
            "title": "Physical & Edge AI: Small Vision-Language-Action (VLA) Models",
            "subtitle": "Extending Sovereign Intelligence into Manufacturing and Smart Cities",
            "bullets": [
                "SmolVLA & Compact Multimodal: Enabling robotic arms and AGVs to interpret physical environments locally.",
                "Intelligent Transport Systems (ITS): Nota.ai smart traffic edge controllers deployed across 200 intersections in Daejeon and Dubai RTA.",
                "Zero Cloud Latency: Real-time visual defect detection and signal optimization at 30 FPS."
            ],
            "visual": "Case illustration: Edge AI controller in smart factory robotic arm and smart city intersection.",
            "notes": "Sovereign AI extends into the physical world. By embedding Small Vision-Language-Action models into edge hardware, we automate factory robotics and smart city traffic in real time.",
            "duration": "8:00 - 8:30"
        },
        {
            "num": "18",
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "The Enterprise Missing Link: Why 85% of AI PoCs Stall",
            "subtitle": "Bridging the Chasm Between Prototype Demos and Production Workflows",
            "bullets": [
                "Hardware Mismatch: Cloud-built prototypes fail when transitioned to corporate datacenter servers.",
                "Data Silos: Fragmented corporate data locked in legacy ERPs, internal PDFs, and legacy databases.",
                "Security Void: Absence of enterprise-grade hallucination guardrails, audit logging, and role-based access control."
            ],
            "visual": "Pipeline diagram showing PoC failure points and MegazoneCloud's end-to-end bridge to production.",
            "notes": "85% of enterprise AI projects stall in prototype phase because integrating chips, models, databases, and compliance is overwhelming. That is the missing link MegazoneCloud resolves.",
            "duration": "8:30 - 9:00"
        },
        {
            "num": "19",
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "MegazoneCloud's 4-Layer Enterprise AI Full-Stack Architecture",
            "subtitle": "The Standardized, Modular Operating Blueprint for Enterprise AI",
            "bullets": [
                "Layer 4 (Applications): Air-Gapped RAG, AI Coding Agents, Executive Decision Portals.",
                "Layer 3 (Model Serving): Nota NetsPresso optimization engine, vLLM, and Triton inference.",
                "Layer 2 (Platform): Red Hat OpenShift AI (RHOAI) and Nutanix Cloud Infrastructure (NCI).",
                "Layer 1 (Hardware): Dell PowerEdge R760, NVIDIA H100 GPUs, and certified K-NPU servers."
            ],
            "visual": "Detailed 4-Layer architectural diagram displaying software logos and interface protocols.",
            "notes": "Our 4-Layer Full-Stack architecture integrates certified hardware, virtualization, optimization compilers, and business applications into a single turnkey solution with one enterprise SLA.",
            "duration": "9:00 - 9:30"
        },
        {
            "num": "20",
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "Deep-Dive: From Nutanix/RHOAI (L2) to vLLM & Nota (L3)",
            "subtitle": "The Engine Room of Low-Latency, High-Density Model Serving",
            "bullets": [
                "Layer 2 Virtualization: Nutanix AHV and OpenShift AI automate GPU resource slicing (vGPU) across departments.",
                "Layer 3 Compilation: Nota NetsPresso profiles hardware and optimizes execution graphs automatically.",
                "Continuous Batching: vLLM PagedAttention ensures sub-second multi-tenant response times under high concurrency."
            ],
            "visual": "Dataflow diagram tracing user query through Nutanix hypervisor to vLLM paged attention cache.",
            "notes": "At Layers 2 and 3, Nutanix and OpenShift virtualize GPU power across departments, while Nota and vLLM maximize inference density, extracting peak performance from minimum hardware.",
            "duration": "9:30 - 10:00"
        },
        {
            "num": "21",
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "Air-Gapped Security & Advanced Graph RAG (Mem0 + Graphify)",
            "subtitle": "True Data Moats: Zero Exfiltration Meets Deep Structural Context",
            "bullets": [
                "100% Air-Gapped Isolation: Zero external bytes transmitted; internal HSM key encryption.",
                "Mem0 Memory Architecture: Multi-session personalized context tracking user security clearance levels.",
                "Graphify AST RAG: Abstract Syntax Tree semantic parsing of enterprise source code and complex manuals."
            ],
            "visual": "Security architecture diagram: Air-Gapped perimeter shield surrounding Mem0 context engine and Graph RAG.",
            "notes": "For banking and defense clients, we build completely air-gapped systems. Using Mem0 memory layers and Graphify knowledge graphs, our AI reasons across corporate manuals without hallucination.",
            "duration": "10:00 - 10:30"
        },
        {
            "num": "22",
            "part": "PART 4: PILLAR 3 - SOLUTIONS & ORCHESTRATION",
            "title": "The ISV Ecosystem: Orchestrating Global & Domestic Innovators",
            "subtitle": "The Power of the MegazoneCloud Multi-Vendor Aggregator Model",
            "bullets": [
                "Global Category Leaders: Articul8 (Autonomous GenAI) and Cohere (Multilingual Enterprise Embeddings).",
                "Domestic Specialist Champions: Nota.ai (Edge Optimization), PuzzleData (Process Mining), QuantumAI (Air-Gapped AICC).",
                "Single Enterprise SLA: Clients get multi-vendor best-of-breed software without contract chaos."
            ],
            "visual": "Partner ecosystem wheel showing MegazoneCloud at center orchestrating global and domestic ISVs.",
            "notes": "We curate the world's finest ISVs. Whether bringing in Silicon Valley's Articul8 and Cohere or domestic champions like Nota and PuzzleData, we orchestrate them into one harmonious platform.",
            "duration": "10:30 - 11:00"
        },
        {
            "num": "23",
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Korea Inc. in Action: Enterprise AI Adoption Across Chaebols",
            "subtitle": "Real-World Deployments Across South Korea's Industrial Giants",
            "bullets": [
                "Semiconductor & High-Tech: Yield prediction, wafer defect inspection, and fab telemetry analytics.",
                "Financial Services: On-premise credit underwriting, automated compliance checks, and private analyst copilots.",
                "Consumer Goods & Beauty (Amorepacific Context): Hyper-personalized beauty formulation compliant with PII laws.",
                "Heavy Industry & Automotive: Assembly line predictive maintenance and CAD engineering assistance."
            ],
            "visual": "Industry mosaic illustrating live deployments across Manufacturing, Banking, Beauty, and Automotive.",
            "notes": "Pillar 4: Real enterprise adoption. In chip manufacturing, AI inspects wafers at line speed. In banking, private LLMs parse regulatory audits. In cosmetics, beauty algorithms run locally on customer data.",
            "duration": "11:00 - 11:30"
        },
        {
            "num": "24",
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Sovereign AI Turnkey Appliance: 1-Click On-Premises Deployment",
            "subtitle": "Delivering Enterprise AI as a Pre-Integrated, Plug-and-Play Appliance",
            "bullets": [
                "Pre-Integrated Hardware: Pre-racked Dell R760 2U server with certified NVIDIA GPUs or K-NPUs.",
                "Rapid Time-to-Value: From power-on to first internal query in under 2 hours (vs. 6 months of consulting).",
                "Built-In Governance: Pre-loaded with Nutanix AHV, Nota NetsPresso INT4, and sovereign domain models."
            ],
            "visual": "Product rendering of the 2U rack appliance showing pre-installed software layers and plug-in setup.",
            "notes": "We package sovereign AI into a plug-and-play 2U appliance. Arrives pre-tested; you connect power and ethernet, and your company has an air-gapped private intelligence platform running in 2 hours.",
            "duration": "11:30 - 12:00"
        },
        {
            "num": "25",
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Measurable Business ROI: 75% Capex Cut & 3.2kW Power Feasibility",
            "subtitle": "The Hard Financial and Operational Metrics of Success",
            "bullets": [
                "Capex Slashed by 75%: $120,000 USD dual-GPU appliance replaces standard $480,000 USD 8-GPU cluster.",
                "Power Draw at 3.2kW: Safely fits standard 10kW datacenter racks, eliminating costly room retrofits.",
                "Latency Reduced 3x: Deterministic sub-50ms token generation for seamless user experience.",
                "Zero Data Exfiltration: 100% compliance with strict national banking and defense security mandates."
            ],
            "visual": "Executive ROI scorecard with side-by-side metric tables and large callout badges (75% SAVINGS).",
            "notes": "These are the metrics that win boardroom approval: 75% Capex savings, 3.2kW power consumption that avoids facility reconstruction, and sub-50ms latency with zero data leakage.",
            "duration": "12:00 - 12:30"
        },
        {
            "num": "26",
            "part": "PART 5: PILLAR 4 - SERVICE & ENTERPRISE ADOPTION",
            "title": "Public Sector & 'AI for All Citizens': National Transformation",
            "subtitle": "Democratizing Artificial Intelligence Across Civil Administration and Healthcare",
            "bullets": [
                "AI Civil Servants: Automating routine civic administration, tax filings, and municipal inquiries.",
                "Universal AI Compute Vouchers: Subsidizing AI compute for 10,000+ domestic SMEs and technology startups.",
                "Healthcare & Rural Equity: Deploying sovereign diagnostic assistants to regional clinics to bridge medical gaps."
            ],
            "visual": "Infographic showing government civic portal, regional hospital diagnostic network, and SME grant flow.",
            "notes": "Sovereign AI is also a public good. Korea's 'AI for All' initiative delivers AI assistants to municipal offices and regional clinics, ensuring technological advancement benefits all citizens.",
            "duration": "12:30 - 13:00"
        },
        {
            "num": "27",
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "MegazoneCloud's Growth Story: From Cloud Pioneer to AI Unicorn",
            "subtitle": "The Operational Architect Behind Korea's Digital Infrastructure",
            "bullets": [
                "1998 to Present: Early digital agency evolved into Korea's first AWS Premier Consulting Partner in 2012.",
                "Official Unicorn (2022): Valuation exceeded $1.8B USD, leading the Korean cloud MSP market.",
                "Scale Today: Over 2,700 enterprise clients, 1,500+ specialized engineers, and multi-cloud market dominance.",
                "The Strategic Evolution: Cloud MSP -> AI MSP -> Global Full-Stack Sovereign AI Orchestrator."
            ],
            "visual": "Milestone timeline spanning 1998, 2012, 2022, and 2026 showing revenue and client expansion trajectory.",
            "notes": "MegazoneCloud pioneered cloud computing in Korea over a decade ago as the country's first AWS Premier Partner. Today, as a multi-billion dollar tech unicorn, we are leading the AI transformation wave.",
            "duration": "13:00 - 13:30"
        },
        {
            "num": "28",
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Global Expansion Playbook: Bridging Korea, US, Japan & SE Asia",
            "subtitle": "Exporting Sovereign AI Methodologies to High-Growth Asian Markets",
            "bullets": [
                "Silicon Valley Hub (Palo Alto): Venture partnerships, co-innovation with frontier AI ISVs.",
                "Japan Expansion (Tokyo): Delivering sovereign on-premise AI to Japanese financial and enterprise leaders.",
                "Southeast Asia (Singapore, Vietnam): Scaling low-power NPU inference appliances and cloud software.",
                "The Strategic Bridge: Connecting Western software innovation with Asian enterprise operational execution."
            ],
            "visual": "Global map linking Silicon Valley, Seoul, Tokyo, and Singapore with active business flows.",
            "notes": "We are expanding globally. Through offices in Palo Alto, Tokyo, and Singapore, we export the sovereign AI methodologies proven in Korea to enterprises across the Asia-Pacific region.",
            "duration": "13:30 - 14:00"
        },
        {
            "num": "29",
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Strategic Takeaways for Global Business Leaders",
            "subtitle": "Key Insights for UCLA Anderson Executive MBA Delegates",
            "bullets": [
                "1. Sovereignty != Isolation: True strategic autonomy combines global technological standards with local control.",
                "2. Datacenter Physics Rule: Power, rack limits, and thermal constraints dictate AI feasibility faster than ambition.",
                "3. Defend Your Proprietary Moat: Internal domain knowledge and proprietary data graphs are your core balance sheet assets.",
                "4. Modular Architectural Agility: Decouple silicon, foundation models, and middleware to prevent future vendor lock-in."
            ],
            "visual": "4 quadrant strategic framework summarizing executive recommendations for global leaders.",
            "notes": "As you return to your executive roles, remember: true sovereignty is about agility, not isolation. Respect datacenter physics early, guard your corporate data, and build modular systems.",
            "duration": "14:00 - 14:30"
        },
        {
            "num": "30",
            "part": "PART 6: MZC PLAYBOOK & GLOBAL VISION",
            "title": "Conclusion & Open Q&A Discussion",
            "subtitle": "Shaping the Future of Enterprise AI Together",
            "bullets": [
                "Presenter: Andy | ISV Business Unit & AI Architecture Group, MegazoneCloud",
                "Official Email: andy@megazone.com | contact@megazone.com",
                "Headquarters: MegazoneCloud Gwacheon Smart Tower, Gwacheon-si, Gyeonggi-do, Korea",
                "Suggested Discussion Topics: Regulatory divergence (US vs. Korea vs. EU), NPU vs. GPU economics, scaling across global subsidiaries."
            ],
            "visual": "Collaborative closing slide with MegazoneCloud and UCLA Anderson logos and live Q&A floor open banner.",
            "notes": "Thank you for your time, leadership, and attention. The future of AI will be shaped by strategic autonomy and global collaboration. The floor is now open for your questions.",
            "duration": "14:30 - 15:00"
        }
    ]

    # 슬라이드별 표 추가 루프
    for s in slides:
        card_table = doc.add_table(rows=5, cols=1)
        card_table.alignment = WD_TABLE_ALIGNMENT.CENTER

        # 행 0: 헤더 (슬라이드 번호 + 파트 구분 + 슬라이드 제목)
        h_cell = card_table.cell(0, 0)
        set_cell_background(h_cell, "003B5C")  # UCLA Navy
        set_cell_margins(h_cell, top=140, bottom=140, left=180, right=180)
        p_h = h_cell.paragraphs[0]
        r_num = p_h.add_run(f"SLIDE {s['num']}  |  {s['part']}\n")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(8.5)
        r_num.font.bold = True
        r_num.font.color.rgb = RGBColor(255, 209, 0)  # UCLA Gold

        r_t = p_h.add_run(s['title'])
        r_t.font.name = "Arial"
        r_t.font.size = Pt(13)
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(255, 255, 255)

        # 행 1: 부제목 & 핵심 테이크어웨이
        st_cell = card_table.cell(1, 0)
        set_cell_background(st_cell, "F0F4F9")
        set_cell_margins(st_cell, top=80, bottom=80, left=180, right=180)
        p_st = st_cell.paragraphs[0]
        r_st = p_st.add_run(f"KEY THEME: {s['subtitle']}")
        r_st.font.name = "Arial"
        r_st.font.size = Pt(9.5)
        r_st.font.bold = True
        r_st.font.color.rgb = RGBColor(0, 59, 92)

        # 행 2: 본문 불릿 포인트
        b_cell = card_table.cell(2, 0)
        set_cell_background(b_cell, "FFFFFF")
        set_cell_margins(b_cell, top=120, bottom=120, left=180, right=180)
        p_b = b_cell.paragraphs[0]
        p_b.text = ""  # clear
        for idx, bullet in enumerate(s['bullets']):
            if idx > 0:
                p_item = b_cell.add_paragraph()
            else:
                p_item = p_b
            p_item.paragraph_format.space_before = Pt(2)
            p_item.paragraph_format.space_after = Pt(2)
            r_dot = p_item.add_run("•  ")
            r_dot.font.bold = True
            r_dot.font.color.rgb = RGBColor(0, 102, 255)
            r_text = p_item.add_run(bullet)
            r_text.font.name = "Arial"
            r_text.font.size = Pt(9.5)

        # 행 3: 비주얼 컨셉 & 아키텍처 제안
        v_cell = card_table.cell(3, 0)
        set_cell_background(v_cell, "FAFBFC")
        set_cell_margins(v_cell, top=70, bottom=70, left=180, right=180)
        p_v = v_cell.paragraphs[0]
        r_v_lbl = p_v.add_run("VISUAL CONCEPT: ")
        r_v_lbl.font.bold = True
        r_v_lbl.font.size = Pt(8.5)
        r_v_lbl.font.color.rgb = RGBColor(100, 110, 120)
        r_v_txt = p_v.add_run(s['visual'])
        r_v_txt.font.italic = True
        r_v_txt.font.size = Pt(8.5)

        # 행 4: 스피커 노트 & 타이밍
        sn_cell = card_table.cell(4, 0)
        set_cell_background(sn_cell, "FFF9E6")  # Light Gold Accent
        set_cell_margins(sn_cell, top=90, bottom=90, left=180, right=180)
        p_sn = sn_cell.paragraphs[0]
        r_sn_lbl = p_sn.add_run(f"SPEAKER NOTES & PACING [{s['duration']}]:\n")
        r_sn_lbl.font.bold = True
        r_sn_lbl.font.size = Pt(8.5)
        r_sn_lbl.font.color.rgb = RGBColor(180, 115, 0)
        r_sn_txt = p_sn.add_run(f'"{s["notes"]}"')
        r_sn_txt.font.name = "Georgia"
        r_sn_txt.font.size = Pt(9)
        r_sn_txt.font.italic = True
        r_sn_txt.font.color.rgb = RGBColor(40, 40, 40)

        # 슬라이드 간 간격
        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(8)
        p_spacer.paragraph_format.space_after = Pt(8)

    # 출력 저장
    output_path = r"c:\dev\antigravity-workspace\aifullstack\K-AI\2026-09-09_Korea_Sovereign_AI_Strategy_Deck.docx"
    doc.save(output_path)
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully generated DOCX: {output_path} ({file_size_kb:.1f} KB)")

if __name__ == "__main__":
    create_sovereign_ai_deck_docx()
