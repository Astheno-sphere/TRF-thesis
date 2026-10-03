

<!-- Start of picture text -->
THE SECOND JOINT ACTION TOWARDS THE EUROPEAN HEALTH DATA SPACE<br><!-- End of picture text -->

**D7.4 Technical specification for Health Data Access Bodies on the implementation of secure processing environments Technical, functional and security specifications of secure processing environments** 

TEHDAS2 – Second Joint Action Towards the European Health Data Space 

24 February 2026 



<!-- Start of picture text -->
atx<br>**<br>**<br>* ¥<br>44%<br><!-- End of picture text -->

**Co-funded by the European Union** 

1 

i 

D7.4 Technical, functional and security specifications of Secure Processing Environments 

# **0 Document info** 

### **0.1 Authors** 

|**Lead Author(s)**|**Lead organisation**|
|---|---|
|**Heikki Lehväslaiho**|CSC – IT Center for Science, Finland|
|**Helena Lodenius**|CSC – IT Center for Science, Finland|
|Beatriz Barros|Sciensano, Belgium|
|Alexandre Berna|Health Data Hub, France|
|Lucas Bréchot|Health Data Hub, France|
|Krisztina Fekete-Molnar|Sciensano, Belgium|
|Zdenek Gütter|Ministry of Health of the Czech Republic|
|Hans Aage Huru|Norwegian Institute of Public Health,<br>Norway|
|Yohan Jarosz|Luxembourg National Data Service,<br>Luxembourg|
|Todor Kondić|Luxembourg National Data Service,<br>Luxembourg|
|Jaakko Lähteenmäki|VTT Technical Research Centre of<br>Finland Ltd, Finland|
|Max Martens|BfArM - Federal Institute for Drugs and<br>Medical Devices, Germany|
|Minerva Alvarez|Spanish Ministry of Health|
|Juha Pajula|VTT Technical Research Centre of<br>Finland Ltd, Finland|
|Thomas Sondag|Luxembourg National Data Service,<br>Luxembourg|
|Christophe Trefois|Luxembourg National Data Service,<br>Luxembourg|
|Emmi Turunen|HUS Group, the joint authority for<br>Helsinki and Uusimaa,Finland|



### **0.2 Keywords** 

**Keywords** TEHDAS2, Joint Action, Health Data, Health Data Space, Secure Processing Environments, SPE Federation, Federated computing ~~<mark>i</mark>~~ 

2 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

### **0.3 Document history** 

|**Date**|**Version**|**Editor**|**Change**|**Status**|
|---|---|---|---|---|
|11/10/2024|0.1|Helena Lodenius, Heikki<br>Lehväslaiho|Table of Contents|Draft|
|27/06/2025|0.2|Heikki Lehväslaiho, Helena<br>Lodenius, Beatriz Barros,<br>Alexandre Berna, Todor<br>Kondić, Jaakko Lähteenmäki,<br>Juha Pajula|Draft to be<br>reviewed by the<br>Consortium|Draft|
|12/09/2025|1.0|Heikki Lehväslaiho, Helena<br>Lodenius, Beatriz Barros,<br>Jaakko Lähteenmäki|Document to be<br>submitted for<br>public<br>consultation|Final|
|02/02/2026|1.1|Heikki Lehväslaiho, Helena<br>Lodenius, Beatriz Barros,<br>Krisztina Fekete-Molnar,<br>Jaakko Lähteenmäki, Juha<br>Pajula, Anne Heidi Skogholt|Draft D7.4|Draft|
|24/02/2026|1.2|Heikki Lehväslaiho, Helena<br>Lodenius, Beatriz Barros,<br>Krisztina Fekete-Molnar|D7.4|Final|



Accepted in Project Steering Group on 24 February 2026. 

### **Disclaimer** 

Views and opinions expressed in this deliverable represent those of the author(s) only and do not necessarily reflect those of the European Union or HaDEA. Neither the European Union nor the granting authority can be held responsible for them. 

### **Copyright Notice** 

Copyright © 2024 TEHDAS2 Consortium Partners. All rights reserved. For more information on the project, please see www.tehdas.eu. 

3 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Table of contents** 

|**_1 Executive summary ............................................................................................................................. 6_**<br>**_2 Introduction ........................................................................................................................................ 7_**|
|---|
|**_3 Scope .................................................................................................................................................. 9_**|
|**_4 Generic SPE ....................................................................................................................................... 11_**|
|**4.1 SPE as service ............................................................................................................................. 11**|
|4.1.1 Principles .......................................................................................................................................................... 11<br>|
|4.1.2 Sensitive data protection requirements .......................................................................................................... 13|
|4.1.3 Enabling needs of scientific research ............................................................................................................... 14|
|4.1.4 Stand-alone SPE ................................................................................................................................................ 16|
|**4.2 SPE federation ............................................................................................................................ 20**|
|4.2.1 SPE federation requirements ........................................................................................................................... 21|
|4.2.2 Federated computing requirements ................................................................................................................ 23|
|**_5 SPE under EHDS ................................................................................................................................. 28_**|
|**5.1 Preliminary life cycle components of EHDS SPE ............................................................................ 28**|
|**5.2 User stories ................................................................................................................................ 29**|
|**5.3 SPE requirements from EHDS Regulation ..................................................................................... 30**|
|**5.4 Functional requirements for EHDS SPE ........................................................................................ 33**<br>5.4.1 Export control ................................................................................................................................................... 33|
|**5.5 Operational requirements for EHDS SPE ...................................................................................... 33**|
|**5.6 Technical interoperability requirements ...................................................................................... 59**|
|5.6.1 Data user and data holder API requirements .................................................................................................. 61|
|5.6.2 Data user remote desktop interface ................................................................................................................ 63|
|5.6.3 SPE service endpoint ........................................................................................................................................ 65|
|5.6.4 Relation to existing specifications .................................................................................................................... 66|
|**5.7 Challenges for EHDS SPE.............................................................................................................. 66**|
|5.7.1 Operational requirements for EHDS SPE federation ........................................................................................ 66|
|5.7.2 Cybersecurity of SPE infrastructure ................................................................................................................. 68|
|5.7.3 Projection to EHDS SPE Federation .................................................................................................................. 69|
|5.7.4 Data access management and SPE interoperability ......................................................................................... 70|
|**_6 Annexes ............................................................................................................................................ 73_**|
|**_Annex 1: Methodology ......................................................................................................................... 74_**|
|**Enterprise Architecture..................................................................................................................... 74**|
|**Modality of requirements ................................................................................................................. 75**|
|**_Annex 2: Public consultation summary .................................................................................................. 77_**|
|**Summary of comments ..................................................................................................................... 77**|
|**Report revisions ............................................................................................................................... 78**|
|**_Annex 3: User journey .......................................................................................................................... 80_**|
|**_Annex 4: Glossary................................................................................................................................. 82_**|



|D7.4 Technical, functional and security specifications of Secure Processing Environments<br>4|
|---|
|**_Annex 5: Historical context and legacy models ...................................................................................... 88_**|
|**Legacy approach: Secret ................................................................................................................... 88**|
|**Legacy approach: Physical isolation .................................................................................................. 88**|
|**Legacy approach: Statistical analysis of registries .............................................................................. 89**|
|**Technical solutions can never be completely secure on their own ...................................................... 89**|
|**Interoperability between SPEs will have a major unifying impact on services ..................................... 89**|
|**_Annex 6: Sensitive data life cycles ......................................................................................................... 91_**|
|**_Annex 7: Design considerations and expert commentary ....................................................................... 93_**|
|**Identity and authorisation ................................................................................................................ 93**|
|**Priority of user training..................................................................................................................... 94**|
|**SPE as collaboration area .................................................................................................................. 95**|
|**Data analysis .................................................................................................................................... 96**|
|**SPE environment management ......................................................................................................... 96**|
|**Monitoring of SPE use ...................................................................................................................... 98**|
|**Data export from SPE ....................................................................................................................... 99**|
|**Scenarios ....................................................................................................................................... 103**|
|**_Annex 8: Existing solutions for secure processing ................................................................................ 106_**|
|**Operational SPEs in Europe ............................................................................................................. 106**|
|**TEHDAS1 ........................................................................................................................................ 108**|
|**Five Safes ....................................................................................................................................... 109**|
|**Trusted Research Environments ...................................................................................................... 111**|
|**DARE UK ........................................................................................................................................ 113**|
|**SATRE ............................................................................................................................................ 113**|
|**EOSC-ENTRUST ............................................................................................................................... 115**|
|**HealthyCloud ................................................................................................................................. 116**|
|**Global Alliance for Genomics and Health (GA4GH) .......................................................................... 117**|
|**GDI and 1+MG ................................................................................................................................ 117**|
|**Sensitive Data HPC strategy (CSC, Finland) ...................................................................................... 118**|
|**NORTRE, infrastructures for sensitive data in Norway ..................................................................... 120**|
|**Secure data transfer solutions (Finland) .......................................................................................... 121**|
|**Anonymity verification tool (Finland) .............................................................................................. 122**|
|**Building a secure health data network (Norway) ............................................................................. 122**|
|**_Annex 9: Overview of relevant EU regulations..................................................................................... 123_**|
|**EHDS article 73 analysis to deduce SPE requirements ...................................................................... 123**|



5 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Key GDPR data and processing requirements .................................................................................. 129 NIS2 Directive ................................................................................................................................ 132** **_Annex 10: Classification of risks and threats against SPEs .................................................................... 134_** 

6 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

# **1  Executive summary** 

This report presents the technical, functional, and security specifications of **Secure Processing Environments (SPEs), a central component of the European Health Data Space (EHDS) as required under Article 73 of Regulation (EU) 2025/327** . SPEs are designed to enable the safe secondary use of electronic health data while ensuring compliance with data protection, confidentiality, and information security obligations. 

Based on a thorough analysis, this report defines **a structured set of minimum requirements for SPEs** . It covers core capabilities needed to safeguard any sensitive data, as well as enabling requirements arising from the needs of scientific research principles. **A generic SPE specification** is developed that is flexible enough to fulfil current and future functional requirements. Functional and operational needs of **two main SPE use cases identified to be needed by EHDS** are shown to be derivable from this model. 

The report goes beyond the obligatory demands of EHDS to define minimal requirements of interoperability between compatible services that form an **SPE-based federation** that is required when data needs to be transferred between organisations. The SPE federation model is further expanded with a set of tentative **practical implementation requirements for federated computing** that is still an active research area. 

The primary purpose of this report is to support policy alignment, harmonised interpretation of legal obligations, and consistent high-level design choices across Member States. It does not aim to serve as a complete practical implementation manual or prescribe specific technologies or architectural solutions. Detailed implementation guidance, reference architectures, and operational playbooks will be developed in subsequent work, including implementing acts, pilot activities and follow-up guidance produced beyond TEHDAS2, for instance by the SPE Community of Practice subgroup. The present document should therefore be understood as a foundation for further specification, standardisation and implementation activities. 

**Justification of the report focus on high-level functional requirements over technical ones is given in the appendices** that cover existing solutions, pitfalls of too narrow approaches, and crucial interplay of SPEs with other services in the ecosystem. Attention is given to how various approaches and technical implementations affect the **trade-offs between data security and usability, how they affect the health data users, and the responsibilities of actors accessing sensitive data.** 

These specifications are intended to support Member States and stakeholders in the design and operation of SPEs and to inform the work of the European Commission in the preparation of the implementing act under Article 73(5) of the EHDS Regulation. 

7 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

# **2  Introduction** 

### **Advancing health data use in the European Health Union** 

<mark>As part of the European Health Union, the European Union (EU) is advancing the use of health data for primary and secondary purposes, including research, innovation and policymaking. Smooth and secure access to data will drive the development of new treatments and medicines and optimise resource utilisation – all with the overarching goal of improving the health of citizens across Europe.</mark> 

<mark>TEHDAS2, the second joint action Towards the European Health Data Space, represents a significant step forward in this vision. The project will develop guidelines and technical specifications to facilitate national and cross-border reuse of health data, and support health data holders, health data users and the new health data access bodies in fulfilling their responsibilities and obligations outlined in the European Health Data Space (EHDS) Regulation.</mark> 

<mark>TEHDAS2 focuses on several critical aspects of health data use.</mark> 

- <mark>Data discovery: findability and availability of health data, ensuring it is accessible for secondary purposes.</mark> 

- <mark>Data access: developing harmonised access procedures and establishing standardised approaches for granting data access across Member States.</mark> 

- <mark>Secure processing environment: defining technical specifications for environments where sensitive health data can be processed safely.</mark> 

- <mark>Citizen-centric obligations: providing guidance on fulfilling obligations to citizens, such as communicating significant research findings that impact their health, informing them about research outcomes and ensuring transparency in how their data is used.</mark> 

- <mark>Collaboration models: developing guidance on collaboration and guidelines on fees and penalties as well as third country and international access to data.</mark> 

<mark>TEHDAS2 will contribute to harmonised implementation of the EHDS Regulation through the concrete guidelines and technical specifications. Some of these documents and resources will also provide input to implementing acts of the regulation. Hence, the joint action will increase the preparedness for the EHDS implementation and lead to better coordination of Member States’ joint efforts towards the secondary use of health data, while also reducing fragmentation in policies and practices related to secondary use.</mark> 

The aim of TEHDAS2 T7.4 deliverable is to develop technical specifications for the lawful and effective operation of Secure Processing Environments (SPEs) in accordance with Article 73 of the European Health Data Space (EHDS) Regulation. These requirements are used to describe functional, security and operational capabilities needed to build SPEs and supporting services. This report defines common concepts, minimum requirements and highlevel specifications for SPEs. The document is intended to support policy alignment, strategic planning and high-level design across Member States and stakeholders. This report is not intended to be a standalone implementation manual. It does not prescribe specific products, detailed configurations, or deployment procedures, and it cannot by itself guarantee 

8 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



operational compliance or certification of SPEs. Implementation requires additional technical documentation, organisational procedures, risk assessments and national choices that are outside the scope of this deliverable. The content presented here should be understood as a framework for future work. More detailed implementation guidance, including reference implementations, interoperability profiles and operational guidelines, will be developed beyond TEHDAS2, in implementing acts of the EHDS Regulation and in national and European initiatives building and operating SPEs in practice. Further details on the methodological approach used to develop these specifications are provided in Annex 1: Methodology. A summary of the stakeholder feedback collected during the public consultation is available in Annex 2: Public consultation summary. 

SPEs must support multiple use cases for secondary data use. Design and implementation choices will significantly influence their ability to accommodate these use cases in a compliant and effective manner. The impact of a precise definition of an SPE will be critical for the context of secondary use of health data. It will guide the use of technologies and capabilities of sensitive data environments across many domains within the European Union and potentially beyond. It is therefore important that the definition of SPE focuses on essentials and enabling the full data management life cycle. 

Health data is inherently dynamic and evolves over time as individuals generate and share information throughout their lives and during medical care. Initially used for direct patient treatment (primary use), this data can later be repurposed for broader goals like public health, research, and policymaking (secondary use). As data moves through various stages – collection, processing, analysis, and storage – it is transformed and enriched, often combined with other datasets. This dynamic flow of information across systems and organisations requires strong collaboration and clear governance. The EHDS aims to give citizens more control over their data and ensure transparency about its use. To achieve data life cycle support, interdisciplinary understanding across legal, organisational, semantic, and technical layers, as outlined in the European Interoperability Framework (EIF), is required. 

This document should be understood as an expert opinion and guidance document developed within the TEHDAS2 framework, reflecting technical and expert input from the project partners. It is not legally binding and does not constitute a formal guideline or technical specification under the European Health Data Space. 

This document does not represent the position of the European Commission. 

Legally binding and enforceable requirements under the European Health Data Space are laid down in Regulation (EU) 2025/327 and, where applicable, in Implementing Acts adopted by the European Commission, within the limits of the empowerments provided by the Regulation. 

9 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **3  Scope** 

This report takes the concept of secure processing environment (SPE) and analyses to ensure the data privacy of processed sensitive data, as well as the privacy and accountability of the user of sensitive data. 

While the context of this report is the EHDS Regulation, the use and applicability of SPE is wider. This has led to several distinct but interdependent sets of requirements where the terminology reflects interpretation of EHDS obligations and recommended minimum standards but does not constitute binding legal requirements beyond the EHDS Regulation. This report is divided into two main parts to separate these sets clearly (Figure 3.1). In addition, requirements dealing with federated aspects of SPE are not mandatory under EHDS Regulation. 

Chapter 4 analyses the general SPE concept first as a stand-alone environment that offers a uniform approach to GDPR requirements. Then it expands its view to a collection of distributed SPEs that need varying levels of interoperability to accomplish increasingly complex computations. The results are presented as a series of requirements aimed at defining high-level design for secure processing that enables scientific research that sets guidelines for policy alignment that is independent of technical implementation details. 

Chapter 5 goes into details analysing how the EHDS Regulation fits into this framework. Specific functional and operational SPE requirements of EHDS legislation are presented and EHDS-specific roles responsible for them are named. The stand-alone SPE, that is a strict requirement of the EHDS Regulation, is analysed separately from the needs of an SPE federation. Technical interoperability requirements for an EHDS-compliant federated learning setup are presented for future reference. 

Annexes give more details of the regulatory analysis, existing solutions of SPEs, and challenges in implementing SPE functionalities. 

Readers are encouraged to familiarise themselves with ArchiMate Enterprice Architecture notation used throughout in figures and the standard modality terminology for requirements that are defined in Annex 1. 

SPEs are critical to enabling lawful secondary use of health data while safeguarding individual privacy and ensuring compliance with GDPR and EHDS Regulations (EHDS SPEs). To clarify the distinction between data processed within the EHDS regulated SPEs and data processed in generic SPEs, it is essential to underline that only EHDS SPEs are subject to legally mandated requirements for access control, auditability, interoperability, controlled outputs, and continuous security monitoring. While generic SPEs may offer technical safeguards, they are not bound by the statutory obligations defined in Article 73 of the EHDS Regulation and therefore do not provide the same level of governance oversight, and protection for secondary use of electronic health data. 

10 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 3.1.** Structure of the report. The ArchiMate graph shows as a work package with the drivers sensitive data protection and scientific research and goals with requirements are numbered with report chapters. Colours are for illustrative purposes. 



<!-- Start of picture text -->
Legal principles ia)<br>GDPR EU ()<br>2016/679)  <]<br>\HH<br>Hi i =<br>re s<br>{ t @ Ne<br>4.1.4, Stand-alone<br>Mandatory es .<br>currentunder SPE <q <} stand-alone SPE<br>0)<br>Future © Ethical and (i)<br>Projection 4,2. SPE federation J foc} principlespractical<br>Chapter 5. SPE under<br>Chapter 4. Generic SPE (high level functional) EHDS (practical,<br>operational)<br><!-- End of picture text -->

11 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **4  Generic SPE** 

### **4.1  SPE as service** 

While cybersecurity and data confidentiality has long history, the European General Data Protection Regulation (GDPR EU 2016/679) precisely defined the defined means and sensitivity of the data. See chapter Key GDPR data and processing requirements in Annex <u>9: Overview of relevant EU regulations</u> and Annex 5: Historical context and legacy models for earlier attempts and consideration to restrict access to data. 

The scope of EU regulation was later expanded to more explicitly mention non-commercial and academic activities.  The European Union Data Governance Act (DGA, EU 2022/868) provides the currently valid definition of SPE: 

**_‘secure processing environment’ means the physical or virtual environment and organisational means to ensure compliance with Union law, such as Regulation (EU) 2016/679, in particular with regard to data subjects’ rights, intellectual property rights, and commercial and statistical confidentiality, integrity and accessibility, as well as with applicable national law, and to allow the entity providing the secure processing environment to determine and supervise all data processing actions, including the display, storage, download and export of data and the calculation of derivative data through computational algorithms_** _;_ (DGA, Article 2) 

We will proceed analysing **SPE as a service** that can be used in multiple use cases, domains of knowledge, and governance structures. We will define high-level requirements of SPEs based on legal drivers and system-level goals. Each set of requirements will need to be defined separately as their scope is wider than following ones that depend on them. 

### **4.1.1  Principles** 

Principles provide justification for service design. Here **, legal principles** are EU-wide laws that guide or define legal requirements. They can be referred to by name or down to a specific paragraph of an article that spell out the specific requirement. The most important laws for SPEs and sensitive data are covered in Annex 9: Overview of relevant EU regulations. 

With respect to service requirements, practical and ethical design principles are best categorised as either **enabling or trust-dependent** ones. Trust covers traditional cybersecurity principles but also wider aspects like privacy and transparency (Figure 4.1). 

12 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 4.1.** Principles affecting the SPE service provision that separates enabling and trustdependent principles. GDPR is the main European legislation determining the application of data confidentiality requirements that balances a wide selection of these principles. 



<!-- Start of picture text -->
Teabie zine Tet<br>TAR o Taga<br>——— ed CRIA i Ta<br>11. 6 112. ‘Administrative (7) Physical (i) pits<br>Seal ristie © security o mB, Comey<br>ae —— __|<br>sustinante © D,<br>Preserve g Protection of a) i<br>‘what works. data donor i<br>western122. Privacy222. of a) iH<br>peep i<br>13. Scalable (f) Transparency lg<br>(ae o a<br>Z<br>1.4. Timely () TAL Pupow Q))2.4. Proportional(242.duadata handling(j) ( 243.Sonoe o<br>thane ee ‘iene<br>1.4.1, State (J)<br>duties<br><!-- End of picture text -->

Enabling principles relate to the benefits and functionalities that SPEs are expected to deliver. These may vary depending on the perspective – for example, from a societal viewpoint (e.g. scientific progress), a service provider’s viewpoint (e.g. performance, scalability, maintainability), or a data user’s viewpoint (e.g. usability, analytical capabilities, cost). 

The most important set of enabling principles data management are FAIR. The combination of findability, accessibility, interoperability and reusability determine how well data and services support scientific research. 

Other enabling aspects gauge if the design is reasonable for current needs (state of the art), it can be maintained with the resources available (sustainable), will be able to respond to ever-changing needs (flexible), and provide services in a timely manner (timely). 

Data confidentiality is a key security principle applied in data management to ensure trust. The GDPR covers all these aspects and requires appropriate measures for confidentiality and integrity based on the level of perceived risk. 

13 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **4.1.2  Sensitive data protection requirements** 

Sensitive data differs from classified data in its requirement to be not only protected but also be available for secure processing 

The sensitive data protection requirements listed in table 4.1 and illustrated in figure 4.2 are sequentially numbered and preceded by the namespace ‘Sensitive Data’ acronym ‘SD’ followed by the letter ‘R’. SDR requirements fall under EHDS Regulation. 

**Table 4.1:** Sensitive data requirements. 

|**#**|**Requirement**|**Source**|**Importance**|
|---|---|---|---|
|SDR-1|Unauthorised persons MUST NOT be able to<br>access sensitive data|GDPR Art. 25, GDPR Art.<br>32|Mandatory|
|SDR-2|Service administrators SHOULD NOT access<br>sensitive data|GDPR Art. 25, Principle<br>2.4.1 Purposelimitation|Recommended|
|SDR-3|Sensitive data MUST be in a protected format at<br>rest andintransit|GDPR Art. 32(1)(c)|Mandatory|
|SDR-4|Sensitive data protection MUST be done with<br>widely accepted, secure algorithms combined with<br>effective isolation measures|GDPR Art. 32(1)(c)|Mandatory|



For a service to process sensitive data, it needs legal basis (GDPR Art. 6 and 9), follow core data protection principles (GDPR Art. 32) and implement appropriate safeguards (GDPR Art. 89). 

All processing of sensitive data must be based on the **sensitive data privacy requirements** . The most important concept is the **authorised user** that identifies persons who have access to the sensitive information contained in the data ( **SDR-1** ). This may be defined as the collector of the information (primary use) or through an explicit permit (as in secondary use). It implements the principles of segregation of duties and least privilege. 

Everyone else is unauthorised, including possible administrators of the service used ( **SDR2** ). In some cases, this may be difficult to maintain, hence this requirement is only a recommendation to allow administrators access when their help is needed in exceptional situations. Security and privacy measures to protect sensitive data should always mention if they are directed to support or control authorised users, deter unauthorised users, or both. 

Sensitive data security is fundamentally based on user identification and the processes used for ID authentication, validation, and verification. Authorisation to access to that is internal to the project that may be defined by an explicit permit. User identification and measures to authenticate users are the foundation of sensitive data security. A high level of identity assurance should be required, and further measures of authentication like multifactor authentication should be adopted. 

To narrow the possibility that sensitive data is available to unauthorised users, it needs to be protected by default ( **SDR-3** ). Encryption is the default way to protect digital information, and it lessens needs to isolate and guard the data. However, this creates the problem of handling encryption keys (secrets management) that need to be present when data will be used. 

Encryption algorithms are constantly improved to answer to new vulnerabilities that technical development brings up. Encryption should rely on peer-reviewed, widely accepted algorithms that are aligned with recognised international standards. Only open encryption algorithms are 

14 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



generally considered safe. Encryption protection is complemented with isolation measures that are either physical, technical or operational ( **SDR-4** ). 

Additionally, pseudonymisation is a widely used method to protect the privacy of individuals from authorised users when they do not need all information and from accidental exposure to unauthorised users.  Pseudonymisation and non-sensitive data types such as anonymised and synthetic data are covered in TEHDAS2 _D7.2 Guideline on data minimisation, pseudonymisation, anonymisation and synthetic data._ 

**Figure 4.2.** General sensitive data protection requirements ArchiMate graph. 



<!-- Start of picture text -->
Sensitive data protection B<br>SDR-1. Unauthorised users MUST NOT be £7<br>able to access sensitive data<br>SDR-2. Service administrators SHOULD NOT 7<br>GDPR (EU in} have access to sensitive data<br>2016/679)  ---><br>SDR-3. Sensitive data MUST be in a protected/7<br>format at rest and in transit<br>SDR-4. Sensitive data protection MUST be 7<br>done with widely accepted, secure algorithms<br>combined with effective isolation measures<br><!-- End of picture text -->

### **4.1.3  Enabling needs of scientific research** 

In this report, we are using scientific research as the ultimate yardstick for the enabling needs of sensitive data processing. In its purest form, scientific research is open-ended. Its results cannot be fully predicted in advance. Unexpected results that give new light to the study area are a real goal of scientific research. Same applies to applications needed to gain these insights: only the researchers themselves who are developing them will be able to evaluate their security and install them. To advance scientific research, users need to be able to perform all these actions. 

Scientific research works as a good representative for controlled, IP-regulated (proprietary, innovation-driven) data processing.  However, not all use cases need wide freedom. A more limited scope for data user makes it possible to simplify and streamline services created for sensitive data processing. Policy making and quality assessment, for example, can be served with services with less user choice. 

The scientific research requirements listed in table 4.2 and illustrated in figure 4.3 are sequentially numbered and preceded by the namespace ‘Scientific Research’ acronym ‘SR’ followed by the letter ‘R’. SRR requirements fall under EHDS Regulation. 

15 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Table 4.2:** Scientific research requirements 

|**#**|**Requirement**|**Source**|**Importance**|
|---|---|---|---|
|SRR-1|Sensitive data protection SHOULD NOT<br>prevent processing for scientific research|GDPR Art. 32(1)(a),<br>Art. 32(2), Art. 89|Recommended|
|SRR-2|Data protection needs MUST minimise impact<br>on application of FAIR principles to sensitive<br>data||Mandatory|



It is important to see that the requirements and functionalities of SPEs depend equally on the restrictive pressure to **protect sensitive data** and the **enabling needs of scientific research** that is a is one of the favoured uses in GDPR restrictions ( **SRR-1** ). 

The need to protect the privacy of the data donor and data processing as expressed in GDPR constrains how the FAIR principles that demand open science principles of findable, accessible, interoperable and reusable are applied to sensitive data ( **SRR-2** ). GDPR primarily affects the accessibility and reusability aspects of FAIR by needing accountability for data access. 

The connection to scientific research helps us to understand the important key difference between sensitive and classified data. Similar methods are used to secure both types of data, but these data types have opposing aims. Secrets are meant to be dangerous facts that society wants to protect and make available for a very limited group of people only when necessary. Protection of sensitive data aims to enable lawful and open-ended research on sensitive data as widely as possible to benefit society. 

Scientific research is a curious combination of society's need to promote the academic curiosity of individuals to reap benefits from their explorations of unknown in a way that unexpected results are common (Figure 4.3). 

**Figure 4.3.** Scientific research requirements. Requirement identifiers follow the convention ‘SRR–n’, where ‘SR’ indicates the scientific research requirements namespace and ‘R’ denotes requirement. 



<!-- Start of picture text -->
Academic<br>curiosity<br>1<br>FAIR fu} Scientific¥research eS<br>Findable (J) Accessible (1) SRR-1, Sensitive data protection SHOULD £7<br>NOT prevent processing for scientific<br>research<br>Interoperable (f) Reusable (J) SRR-2. Data protection needs MUST [7<br>minimise impact on application of FAIR<br>principles to sensitive data<br>*<br>H<br>Benefit to<br>the society<br><!-- End of picture text -->

16 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **4.1.4  Stand-alone SPE** 

When applying the wide and risk-based requirements from general sensitive data protection to GDPR-based standalone SPE according to its DGA definition, they can be reduced to two main security conditions: monitoring and isolation (Figure 4.4). 

**Figure 4.4.** Legal conditions of SPE 



<!-- Start of picture text -->
GDPR(EU (1) Sensitive<br>2016/679) — ------------------> data<br>protection<br>T<br>'<br>{<br>¥<br>Secure Processing Environment (SPE) ®<br>Organisationalmeasures 7<br>11<br>ii<br>v ¥<br>Data Governance (1) SPE SPE<br>Act (EU +---> definition: definition:<br>2022/868) Monitoring Isolation<br>'i<br>vv<br>Secure ©<br>environment<br>SPE physical © SPE virtual ©<br>environment (computer)<br>environment<br><!-- End of picture text -->

In this context, we can ignore the physical environment and focus on SPE as a virtual computer environment. Then we can say that **SPE operators** provide a secure service that isolates sensitive data processing within its confines.  Isolation is provided based on projects that are separated from each other. The monitoring covers service access, data transfers, and of course the success of the isolation (Figure 4.5). 

Users have access to their **project space** that contains their sensitive data. The project space has the ability store and process sensitive data. For **data users** , this project space is their “SPE” that is different from the SPE service. This difference between the two SPE concepts has been a source of much confusion. 

17 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Figure 4.5.** Strategic view of a generic SPE. SPE is represented as abstract ArchiMate capability that has resources it needs to have or react to. 



<!-- Start of picture text -->
Generic SPE<br>Monitoring wo<br>+ verify ——————_ Access (i> Data @> = —————~-Prevent<br>transfer |<br>Secure Processing Environment (SPE) fl Exeral actors<br>Non-project (i)<br>Project wo Import Project@ space Analysis Gi)wo users<br>User SPE wo<br>jet servey— management<br>Tools > Export GD<br>Hostiles Gi}<br>Isolation (i) |<br>+ proteet———_—_——_—_—— =- repel<br><!-- End of picture text -->

The general purpose SPE requirements listed in table 4.3 and diagrammed in figure 4.6 are sequentially numbered and preceded by the namespace acronym ‘SPE’ followed by the letter ‘R’. SDR requirements fall under EHDS Regulation. 

**Table 4.3:** Stand-alone minimum SPE requirements 

|**#**|**Requirement**|**Source**|**Responsible**<br>**role**|**Importance**|
|---|---|---|---|---|
|SPER-1|SPE MUST enable<br>scientific research on<br>sensitive data|SSR-1|SPE Operator|Mandatory|
|SPER-2|There SHOULD be a<br>diverse selection of<br>SPEs for the varied<br>needs of sensitive<br>dataresearch|SSR-1|SPE Operator|Recommended|
|SPER-3|It MUST be possible to<br>transfer sensitive data<br>between, in and out of<br>SPEs|SSR-1, SDR-3|SPE Operator|Mandatory|
|SPER-4|SPE MUST provide<br>adequate protection<br>against exposing<br>sensitive data to<br>unauthorised users|SDR-1, SDR-2|SPE Operator|Mandatory|
|SPER-5|SPE design SHOULD<br>promote collaboration|SRR-2|SPE Operator|Recommended|



18 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

||among authorised<br>users||||
|---|---|---|---|---|
|SPER-6|Authorised users<br>MUST protect<br>sensitive data they<br>display|SDR-3|Data User|Mandatory|
|SPER-7|Project-based user<br>environments of SPE<br>MUST NOT have open<br>connections|SDR-3, SDR-4,<br>SPE definition:<br>Isolation|SPE Operator|Mandatory|
|SPER-8|SPE user accesses<br>and data transfers<br>MUST be logged and<br>monitored|SDR-4, SPE<br>definition:<br>Monitoring|SPE Operator|Mandatory|



SPE has been defined to meet the demands of scientific sensitive data processing and, by extension, other uses that need high level of protection ( **SPER-1** )<sup>1</sup> . 

Openness and interoperability as expressed in the FAIR principles are essential elements of scientific research. In the context of sensitive data processing, they also embody the unpredictability of scientific research results that must be considered in the SPE design. Since it is impossible to determine beforehand what twists and turns empirical scientific research will take, the functional definition of an SPE must be open-ended. In other words, we cannot limit the SPE capabilities _a priori_ . 

Hardware and software capabilities of SPE instances is and will remain to be variable. It is impossible for any single SPE to fulfil all present and future requirements. Data capacity and analysis capabilities will differ widely and create a market for different SPEs ( **SPER-2** ). 

For users, the primary advantage of SPE is the compliance to GDPR requirement that allows them to focus on data analysis. In the default case, the users are primary controllers of sensitive data and they need the ability to move code, applications and sensitive data as they please for processing in the safe environment that SPE provides ( **SPER-3** ). These abilities may be limited by data permit if the sensitive data is under controlled access secondary use. 

Activities that create sensitive data are out of scope but to make datasets available for analysis they need to be transferred into an SPE. Also, the diversity and changing needs of research might make it necessary that sensitive data must be transferred between SPEs during the analysis. This does not mean that that transfer is necessary direct. 

Users should be able trust the technical functionalities the SPE is providing ( **SPER-4** ). 

SPE users have the right to expect that basic tools needed for their analysis, and more generally conducting their research on sensitive data, are supported by the SPE service ( **SPER-5** ). This could include a collection of preinstalled common libraries and tools but also more comprehensive collaboration among project members (See Annex 7: Design <u>considerations and expert commentary – SPE as collaboration area).</u> 

A related and resolved issue is the SPE support to anonymous reviewing of results in cases where sensitive data is prohibited to be exported out of the SPE. SPE service might respond to this by making it possible to have unidentifiable aliases to users. 

> 1 The 2025 ruling by the European Court of Justice on lesser sensitivity of pseudonymised personal data is included in the Digital Omnibus legal package under preparation. It could have impact on SPE use. 

19 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



Authorised users must bear the responsibility of their actions. For most of the expected SPE use, authorised users display plain-text sensitive data on their computer screens, and they must be aware that it is their responsibility to protect it ( **SPER-6** ). 

Monitoring displayed sensitive information in modern distributed and virtualised environments is hard. If the use of SPE is made too cumbersome for technical or regulatory reasons, users are easily tempted to take note of the displayed information from the screen rather than follow official ways. In practice, this means that any addition of any security measures that limit the ability of authorised users to process sensitive data need to be evaluated against this danger. Ultimately there are no foolproof technical means to ensure that users do the right thing, or even that they know what that is. It is therefore necessary to ensure that SPE users have the proper understanding of their responsibilities. See Annex 7: <u>Design considerations and expert commentary – Priority of user training.</u> 

Stand-alone SPEs must be by default designed in such a way that user environments within it are clearly and completely isolated from each other and from the open Internet ( **SPER-7** ). Any explicitly opened connections must be secure. This is needed for both control and protection of the environment. We will see that there are many practical reasons to open connections in controlled way to meet real world needs. 

The first of them applies to use cases where users are primary controllers of the sensitive data. They might want to give access to other projects within the same SPE. Secure sharing of datasets can then be part of the SPE interface, and projects can focus on the contractual side of the transaction. 

Monitoring and logging are requirements that include transparency and data minimisation under GDPR and are also mentioned in the SPE definition. The requirement **SPER-8** takes the stand balance to risk and feasibility as required by GDPR Article 5(1)(c) and Article 32 that access logs and data transfer logs are crucial to monitor and contain useful information. User action logs are seen to be coved by user privacy and unlikely to contain useful information in its impractically massive volumes. See the reasoning in more detail in Annex <u>7: Design considerations and expert commentary – Monitoring of SPE use</u> 

20 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 4.6.** SPE minimum requirements and their derivation. Requirement identifiers follow the convention ‘SPER–n’, where ‘SPE’ indicates the general purpose SPE requirements namespace and ‘R’ denotes requirement. SPER requirements fall under EHDS Regulation. 



<!-- Start of picture text -->
SPE virtual (computer) environment minimum ©<br>Scientific research 8 one<br>|(SRR=1,NOT preventSensitiveprocessing data protection SHOULD £7 (SPER-1. SPE MUST enable scientific research on 7<br>research for scientific. || ~—=~>= ===> >= oma enoneng\ sensitive data, y)<br>(/_SRR-2. Data protection needs MUST £7 H (_SPER-2. There SHOULD be a diverse selection of £7)<br>minimiseprinciples impact toon sensitive applicationdataof FAIR. ~~~~>~~~~~--~~>,' {Lg' SPEs for the varied needs of sensitive data research }|<br>' i SPER-3. It MUST be possible to transfer sensitive<br>'<br>tata es data between,in and out of SPES<br>‘ Sensitive data protection eS 'y H‘ zs _/” against(-SPER-4, exposing SPE MUSTsensitive provide dataadequate to unauthorisedprotection [7<br>( j vo \ users<br>| SDR-1.CID Unauthorised CETE CRINGE users MUST NOT be £7) f4----4 H' ““ “SSESPER-5.NT RR SPE SHOULDRON promotea collaborationaE ET among<br>L Ln Seee authorised users,<br>( SDR-2. Service administrators SHOULD NOT 7 i “ DS<br>| hhave access to sensitive data P--" ceri ES EE<br>format at rest and in transit Environment (SPE)<br>|(SDR-3. Sensitive data MUST be in a protected] (Secure Processing © CET ECE EY<br>a =) SPER-7. Project-based user environments of SPE [7<br>‘SDR-4, Sensitive data protection MUST be [7)------- al wee | PTS MS OCLC<br>done with widely accepted, secure algorithms N<br>| NGECE<br>—eewv—wo—owerwresesseeerv‘combined with effective isolation measures = caves SPER-8. SPE user accesses and data transfers MUST<br>definition: --~-------—>» be logged and monitored<br>Monitoring<br><!-- End of picture text -->

### **4.2  SPE federation** 

The preceding analysis of SPE requirements described a service that is strictly an independent service. Its legal definition stresses the legality, security and accountability of sensitive data processing as if there were only one of SPE. Having all data needed for a project in one SPE remains the main use case, but there are situations where it is not possible. This chapter expands those requirements to many SPEs and interoperability between them. Any means to enable data processing in more than one environment is called distributed processing. 

The first stage of interoperability needs to come from the set of services that fall under the same category. From both policy and user point of view it is necessary to know how many there are, and in what respects they differ from each other. There is a need for a findability service that in turn needs a shared vocabulary that is used to build a registry of services. 

Services like SPE that need data must have means to transfer data in and out, as well as programmes implementing algorithms to process the data. Convenience together with security concerns pushes these to follow common practices. Users and data managers have the need to utilise different capabilities of SPE services that change over time. 

SPE was envisioned as a convenient place that needs a set of safety rules to perform calculations on sensitive data. The need to provide continuous protection to sensitive data 

21 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



in a distributed world has led to ecosystem thinking like in European data spaces. Within them, SPE functionalities and safety requirements need to cover all aspects of data processing. Under European laws, this processing is best organised using SPEs through which users interact with sensitive data. 

### **4.2.1  SPE federation requirements** 

Interoperability works best when it is defined in hierarchies with a tightening set of rules and their applications. A general federation covers the most fundamental interoperability rules, next one defines a domain, next a use case, always building on top of previous rules. This way a project involving SPEs in different countries is a federation defined by the data permit that provides the contractual basis. 

We sketch this out by defining base requirements for SPE federations in table 4.4. 

**Table 4.4:** Minimum SPE federation requirements. The requirements of general purpose SPE federation have the namespace acronym ‘FSPE’ for Federated SPE followed by the letter ‘R’. FSPE requirements do not fall under EHDS Regulation. Importance levels of its requirements are valid only within its namespace. 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|FSPER-1|Legal or contractual agreement MUST cover the SPE federation across<br>organisations|Mandatory|
|FSPER-2|Federation user identities MUST match over services|Mandatory|
|FSPER-3|SPE federation environment MUST fulfil sensitive data processing<br>requirements ofstand-alone SPEs|Mandatory|
|FSPER-4|All interactive user actions on sensitive data in the federation MUST be<br>throughSPE|Mandatory|
|FSPER-5|Federation governance structure MUST cover secure, shared data access<br>and exportfromSPE|Mandatory|
|FSPER-6|Federation user identities SHOULD be shared|Recommended|
|FSPER-7|Federation SPEs MUST share technical and semantic interoperability<br>neededforshared processing|Mandatory|
|FSPER-8|Federation SPEs MUST use shared secure communication and data<br>transferprotocols|Mandatory|
|FSPER-9|The federation MUST support distributed processing through authorisation<br>and accounting services|Mandatory|
|FSPER-10|A federation SPE MAY fulfil federated computing requirements|Optional|



A formal agreement between SPEs is the foundation of an SPE federation ( **FSPER-1** ).  The rules of federation must be based on writing for transparency and enable shared sensitive data processing across organisations. 

An SPE federation needs ways to identify and authorise its users in all federation services ( **FSPER-2** ). This can be done by matching local identities over federated identities. An SPE federation is based on SPEs providing the main sensitive data protection. None of the stand-alone SPE rules should be violated in an SPE federation ( **FSPER-3** ). 

While the aim of the SPE federation is to widen the scope and quantity of sensitive data processing via automated, remote processes, the users must log in to an SPE to initiate the 

22 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



processing and export the results ( **FSPER-4** ). The customary external programmes that control the processing in general federated computing, are not allowed. 

The federation will need to provide the governance structure that defines operational procedures for secure, shared processes for data transfer ( **FSPER-5** ). 

While the federation can function with matching user identities as required in FSPER-2, its authorisation services are significantly strengthened by a federation-wide identity system **FSPER-6** . This is a nod of approval towards the shared European eiDAS system.  A shared user identity system may enhance service authorisation and auditability to better comply with GDPR principles. 

Shared processing needs agreements on technical and semantic standards that will enable it ( **FSPER-7** ). In a European context, the most common health data model for remote data queries is OMOP CDM. 

Security of communication between federation members, especially when transferring sensitive data, is the fundamental requirement ( **FSPER-8** ). EU eDelivery and GA4GH crypt4GH are examples of these (see chapter <u>Data access management and SPE interoperability).</u> 

A federation needs – usually centrally managed – registries that secure non-interactive, distributed processing. While authorisation has been traditionally been an integral part of grid computing, accounting and billing has been ignored to the detriment of long-term sustainability of the service ( **FSPER-9** ). Federation registries need to have infrastructure metadata about its authorised services and service providers, content metadata for dataset discoverability, and governance metadata about data permits that link project and users to datasets and resource usage<sup>2</sup> . 

Specialised distributed computing methods are usually called federated computing that is a separate set of requirements that are based on federation principles ( **FSPER-10** ). Federated processing is its own branch of distributed processing that some members of the SPE federation may enable (See chapter Federated computing). 

2 DARE UK Federated Architecture Blueprint https://doi.org/10.5281/zenodo.14192786 

23 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 4.7.** SPE federation requirements. 



<!-- Start of picture text -->
SPE federation requirements ©<br>Federation functional requirements ©<br>Legal or FSPER-1. Legal or contractual agreement MUST FSPER-6. Federation user identities SHOULD 7<br>contractual <----- cover the SPE federation across organisations -~>,---> be shared<br>agreement if<br>FSPER-2. Federation user identities MUST P\__\.! FSPER-7. Federation SPEs MUST share technical]<br>® match over services 5ry ye and semanticsharedinteroperabilityprocessing needed for<br>SPE virtual - hike<br>(Cais) FSPER-3. SPE federation environment MUST 7) | | ‘x FSPER-8. Federation SPEs MUST use shared 7<br>environment -~~+-> fulfil sensitive data processing requirements of | secure communication and data transfer<br>anor stand-alone SPES it protocols<br>Rana H i<br>FSPER-4. All interactive user actions on 7)! | FSPER-9. The federation MUST support 7<br>sensitive data in the federation MUST be | b->> distributed processing through authorisation<br>through SPE in and accounting services,<br>FSPER-5. Federation governance structure S)\__/ FSPER-10. A federation SPE MAY fulfil 57<br>MUST cover secure, shared data access and S___. federated processing requirements<br>export from SPE<br><!-- End of picture text -->

### **4.2.2  Federated computing requirements** 

### **Scope and definitions** 

This section provides a proposal for supporting federated computing within the SPE federation defined in the previous chapter. A high-level conceptual architecture is presented. The impact of federated computing on the data permit application phase, including how the involved SPEs are selected by the health data user and approved by the HDAB is out of scope of the deliverable. 

A wide variety of definitions related to federated computing exist. For the EHDS implementation purposes, it is important to distinguish between two scenarios: (1) cases where node outputs are anonymous and can be directly returned to data users, and (2) cases where the anonymity of node outputs cannot be fully guaranteed. The terms **“federated analysis”** and **“federated learning”** are used to describe these scenarios, respectively. This categorisation aligns with the different needs of data users and supports the possibility of gradual implementation of federated computing, starting from simpler and less resourceintensive setups. 

It is also important to note that, the EHDS Regulation does not mandate that HDABs to provide federated computing services. 

**Federated computing**<sup>**3**</sup> is a decentralised data processing approach where computations occur locally on distributed SPEs rather than being centralised into a single SPE. Such approach is encouraged by EHDS Regulation (Recital 80) which promotes the principle of “bringing algorithms to the data” to enhance privacy-preserving computation. Federated computing methods enable data to remain closer to their original location while only aggregated results or model updates are shared, enhancing privacy and security. 

> 3 Federated computing is not mandated under the EHDS Regulation, but may be supported under future implementing acts (Article 73(5)) 

24 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Federated analysis** is a form of federated computing in which each participating SPE performs local computations and returns results that can be considered anonymous by design (e.g., aggregated or statistical outputs). These results can be directly combined by a coordinating entity (the data user application, see Section 5.6) without additional anonymisation steps. This method enables benchmarking, multi-site research, and collaborative analytics while preserving data privacy and security. 

**Federated learning** is a form of federated computing in which participating SPEs collaboratively train models by exchanging intermediate results (such as model parameters or gradients). Individual-level data are not exchanged between SPEs. Instead, only model updates are communicated thereby enhancing data privacy and security. In this case, the anonymity of exchanged information cannot be fully guaranteed, and additional privacypreserving and trust mechanisms may be required. Federated learning may involve information exchange between computing nodes under defined mutual trust conditions. 

Due to the difficulty of assessing the anonymity of intermediate outputs, it is essential that federated learning computation and information exchange takes place within a network of trusted SPEs (the SPE federation). 

#### **High-level federated architecture** 

The proposed federated computing approach aligns with Recital 80 of the EHDS Regulation, which encourages bringing questions to the data instead of moving the data. However, the EHDS Regulation does not provide further direction on how to support the implementation of federated computing.  Further guidance is expected in the context of implementing acts concerning secure processing environments. 

Two settings can be identified. In the first (Figure 4.8.a), the health data user’s application interacts independently with multiple SPEs via API interface, retrieving anonymised outputs from each and combining them to compute statistical results. In this case, no communication occurs between SPEs. A prerequisite for this setting is that the SPE operator provides an API interface and related governance processes as outlined in Section 5.6. 

Figure 4.8.b illustrates a second setting where a master SPE (SPE#1) communicates with other SPEs to perform a federated learning task. The master SPE is responsible for orchestrating the federated learning process, collecting computation results from the other SPEs to iteratively train or validate a machine learning model. The health data user retrieves the final output (e.g., the trained model) from the master SPE after privacy risk assessment and disclosure approval by the HDAB (see TEHDAS2 deliverable D7.2). 

A prerequisite for this setting is that the SPE operator provides an open and standardised interface needed to exchange information with other trusted SPEs as outlined in Section 5.6. Furthermore, an SPE federation (see <u>SPE federation) is a prerequisite for the setting of</u> Figure 4.8.b to establish the framework for communication between trusted SPEs. In order to further minimise and control risks of personal data leaks the SPE operator may support and require the use of privacy protection methods (such as differential privacy). 

25 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 4.8.** (a) Data user application collects and further processes anonymous computation results from multiple SPEs. (b) Data user application is connected with one master SPE, which in turn communicates with other SPEs under trust conditions to accomplish a federated computing task. 



<!-- Start of picture text -->
Adatanonymous<br>SPE #1 exchange<br>Caz data user<br>application<br>SPE #3<br><!-- End of picture text -->



<!-- Start of picture text -->
Data exchange between<br>SPE #2 SPE’s5  under trust conditions<br>SPE #1 ata user<br>Anonymous  @PPlication<br>data<br>SPE #3 exchange<br><!-- End of picture text -->



<!-- Start of picture text -->
(a)  (b)<br><!-- End of picture text -->

The scenario illustrated in Figure 4.8.a is relevant for federated analysis use cases, where only anonymous aggregated results need to be transferred to the health data user by each SPE. Figure 4.8.b is relevant for federated learning use cases, where it is difficult to ensure the anonymity of the interim outputs of the SPEs and which thus need to be kept within the network of federated SPEs. 

#### **Assumptions** 

Proposed functional requirements for supporting federated computing are based on the following assumptions: 

- Federated computing is applied in the framework of the EHDS Regulation complemented by more detailed specifications (e.g. implementing acts) 

- All computations on sensitive personal data are carried out in an SPE environment aligned with EHDS requirements (e.g.  Article 73 of the EHDS Regulation) 

- All SPE services involved in federated computing are EHDS compliant, trusted, audited and under control of HDABs or trusted data holders (directly or through data processing agreements with SPE operators). 

- SPEs involved in federated computing, i.e. **SPE federation,** may be located in one or more countries. 

- Federated computing support is a recommended but optional feature of an SPE (“MUST” in a requirement means that the requirement is applicable if federated computing is supported by the SPE). 

- An SPE may also support only a subset of federated computing requirements, e.g. limiting to federated analysis. 

26 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



- All data resources used in a federated computing setup shall be covered by the same data permit, with approval by the relevant HDABs or trusted health data holders. 

#### **Functional requirements** 

The requirements of computing performed by a federation of SPEs are listed in Table 4.5. These requirements have the namespace acronym ‘FC’ followed by the letter ‘R’. FC requirements cannot be derived directly from the EHDS Regulation but will be subject to it if these processes are used for secondary use of health data. Importance levels of its requirements are valid only within its namespace. 

**Table 4.5:** Functional requirements of computing performed by a federation of SPEs. 

|**#**|**Requirement**|**Importance**|**Role**|
|---|---|---|---|
|FCR-1|SPE project space MUST support a shared<br>data model|Mandatory|SPE operator|
|FCR-2|Controlled and secure data transfer<br>supporting federated computing MUST be<br>enabled between the participating SPE project<br>spaces|Mandatory|SPE operator|
|FCR-3|Participating SPE project space MUST support<br>the deployment and execution of software<br>components needed|Mandatory|Data user|
|FCR-4|The project MUST be authorised to use<br>federated computing|Mandatory|Data controller|



The effect of these functional requirements is illustrated Figure 4.9. to project a vision of a federated SPE that communicates to other members of the federation through isolated secure gateways (security server). The main practical implications are that 1) the data accessible to users must be independently accessible to (permitted) federation services and that 2) security of the encrypted data needs to be maximised, preferably by dynamic, onetime keys managed by a dedicated secrets management component of SPE. 

27 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 4.9.** Projection of functional requirements for SPE in a federation. Motivation elements (violet) show the justification and strategy elements show how all communications to SPE and the user’s project environment must go through isolated gateways within the security server that has its counterparts in all federation resources. 



<!-- Start of picture text -->
SPE MUSTaccesspreventto unauthoriseddata 7<br>a H<br>' Federation SPE ao<br>v Control may be Encryption key<br>es conc e sar)ties 0 Ste one ETE andinstantiated conditions, by terms May be temporary Permanentfor the | couldmanagementbe managed<br>project<br>controlled contracts, and permits by the federation<br>¥<br>‘ThereandMUSTfederationbe trustresourcesbetween SPE7 Securd Processing Environment (SPE) F<br>; Project environment oD<br>SPE user MUST bex  able to open [7 Compute GD Storage OD) Secrets (|<br>controlled, two-way connections = ‘+ management<br>to federation resources<br>|1ee~~ Permitted federation resources [7 |<br>, SHOULD be accessible to SPE<br>iaSuser ky} Security server wo<br>|<br>| Identified SPE storage items 7<br>| MUST be accessible to<br>' federation resources Federation resources Do<br>' Identity management GD)<br>| (Identified SPE data secrets MUST<br>St be accessible to federation<br>resources 7 ser Q<br><!-- End of picture text -->

28 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

# **5  SPE under EHDS** 

### **5.1  Preliminary life cycle components of EHDS SPE** 

The use of an SPE within the HealthData@EU infrastructure occurs after a health data user (in distinction from the generic SPE user that is called _data user_ ) has been granted access to a specific dataset and a data permit has been issued by the HDAB<sup>4</sup> . The general life cycle of an SPE, as outlined in TEHDAS1<sup>5</sup> , consists of the following steps: 

**Environment Creation** : Once the data permit is issued, the designated SPE operator sets up an isolated environment instance, tailored to the health data access application form. In the current IT landscape, this may be done by deploying a virtual machine or container, either in a dedicated cluster or a cloud computing environment. 

**Data Reception** : Depending on the interface arrangements between the SPE and the data holder(s), data can either be pulled by the SPE operator from the data holder(s) or pushed by the data holder(s) to the assigned SPE storage. 

**Data Upload** : HDABs may use an _intermediate_ SPE to prepare the data. This includes anonymisation or pseudonymisation, as well as data linkage (combining the datasets requested by the applicant at individual level). Pseudonymisation ensures that data cannot be linked to an individual without access to a separate key, which only the HDAB holds. Once the data, sometimes from several data holders, have been prepared, all of it is securely transferred from the intermediate SPE to a user-facing SPE. 

**Data Analysis** : The health data user then processes the uploaded data within the environment using the tools provided in that SPE instance to derive the insights they are seeking. 

**Results Extraction** : Once the analysis is complete, the health data user must request permission to download the fully anonymised aggregated results (whether partial or final) from the SPE. This step involves controlling and monitoring the data that is allowed to leave the SPE by the HDAB. 

**Environment Decommissioning/Archival** : After the project concludes or the data permit expires, the environment may either be decommissioned (with all contents destroyed) or archived for potential future use, under new conditions, such as for reproducibility of results or new project permits. 

> 4 D6.2 Guideline for data users on good application and access practice https://tehdas.eu/wpcontent/uploads/2025/10/d6.2-guideline-for-data-users-on-good-application-and-access-practice.pdf 5 D7.2. Options for the services and services architecture and infrastructure for secondary use of data in the EHDS https://tehdas.eu/tehdas1/results/tehdas-proposals-for-the-implementation-of- <u>ehds-technical-infrastructure/</u> 

29 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 5.1.** The SPE functionalities as specified in the TEHDAS1 project. 



<!-- Start of picture text -->
Data =) EHDS Art. (1)<br>Governance — <P— 73<br>Act, Art.2(14)<br>4<br>Secure ff<br>Processing<br>Environment<br>Project @ Data upload Gi) Data wD Results (i> Project wo<br>environment analysis extraction environment<br>creation decommissioning<br><!-- End of picture text -->

### **5.2  User stories** 

In the context of the EHDS framework, two typical user profiles can be distinguished in relation to the use of SPEs, HDAB and health data user, each associated with different roles, restrictions, and levels of responsibility. 

We must differentiate the two uses of the term SPE. For the SPE operator, it is a service that must be maintained to its users. SPE is also used to refer to collective functionalities of SPE user accessible instances. For users, SPE is a project-based environment that is fully separated from other project environments within the service. To distinguish these, the full term for the latter would be **SPE project-based user space** . Any shorter versions of this should include either ‘user’ or ‘project’ to be clear what environment is meant. 

The main use case is the one where the user is the health data user processing health data for secondary use according to a data permit. The whole process is overseen by an HDAB that provides the prepared sensitive data to the user, and the user is not allowed to export anything but anonymous results out of the SPE. 

The second use case defines the HDAB itself as the user. An HDAB employee must do the final processing of the permitted health data that in the next stage will be handed over to the health data user’s SPE environment. The HDAB user is fully responsible for both managing the import of datasets, possibly from multiple health data holders, and export of the final permitted dataset with personal details. This use case utilises SPE solely to protect the health data and its processing from non-users. It is subject to general access control monitoring of services, but nothing more. In wider context, this matches the requirements of generic scientific research SPE protecting any sensitive data processing shown in Figure 4.5. 

These two use cases reflect different trust and control models, which have implications for design of SPEs and how technical and operations measures (TOMs) are implemented. To emphasise the importance of trust, we name these **distrusting and trusting use cases** 

30 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

(Figure 5.2). The challenge is to understand the implications of both use cases to the functional and technical design of SPE. 

**Figure 5.2.** SPE trusting and distrusting use cases. 



<!-- Start of picture text -->
SPE distrusting use case<br>SPE trusting use case<br>PSE iperaltant Monitoring oO<br>+ verify ———— Access Data. @| += prevent<br>transfer |<br>data access ‘Secure Processing Environment (SPE) if] eenmicreo Gay<br>eeitation Non-project GD)<br>Project space [cry users<br>Project «| impor | Analysis<br>monitoringProcess GD User <+ serve managementsre oD<br>Tools @ Export @<br>Tool @, Hostiles D<br>limitation<br>Eganes (1 Isolation GD)<br>anonymous<br>results only + protect —————~ - repel<br><!-- End of picture text -->

### **5.3  SPE requirements from EHDS Regulation** 

Article 73 of the EHDS Regulation lists baseline legal requirements for SPEs, serving as a foundation and minimum standard for the guidelines. Article 73(5) provides the empowerment for further implementing acts that this report aims to advise. 

Article 73 requires that all processing of electronic health data for secondary use purposes must take place in a secure processing environment (SPE). These environments must have robust data protection processes, restricted unauthorised access, and prevent data from being copied or transferred unlawfully. SPE providers must comply with relevant EU laws, ensuring transparency and oversight to maintain trust and privacy. 

Requirements derived from Article 73 are listed in table 5.1 and in Figure 5.3. The detailed analysis of Article 73 and derivation of its requirements is provided in Annex 9: EHDS article <u>73 analysis to deduce SPE requirements.</u> 

The functional and operational requirements of SPEs derived from the EHDS Regulation have by the namespace acronym ‘EHDS’ followed by the letter ‘R’. These requirements and their importance are interpretations of the EHDS Regulation. 

31 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Table 5.1:** Functional and operational requirements of SPEs derived from the EHDS Regulation. 

|**#**|**Requirement**|**Source**|**Responsible**<br>**role**|**Importance**|
|---|---|---|---|---|
|EHDSR-1|HDAB MUST grant<br>access to EHD using a<br>data permit|EHDS Art. 73(1)|<br>HDAB|Mandatory|
|EHDSR-2|EHD MUST be<br>accessed using an<br>SPE|EHDS Art. 73(1)|HDAB|Mandatory|
|EHDSR-3|Natural persons listed<br>in the data permit MAY<br>access the identified<br>EHD inSPE|EHDS Art. 73(1)(a)<br>and (c)|HDAB, SPE<br>Operator|Mandatory|
|EHDSR-4|<br>TOMs MUST minimise<br>the risk of<br>unauthorised EHD<br>accessinSPEs|EHDS Art. 73(1)(b)|HDAB, SPE<br>Operator|Mandatory|
|EHDSR-5|<br>Authorised health data<br>users MUST be<br>stronglyidentified|EHDS Art. 73(1)(c)<br>and (d)|HDAB, SPE<br>Operator|Mandatory|
|EHDSR-6|All access and<br>operation logs of SPE<br>MUST be available for<br>verification and<br>auditing|EHDS Art. 73(1)(d)<br>and (e)|SPE Operator|Mandatory|
|EHDSR-7|All SPE logs MUST<br>identify the actor|EHDS Art. 73(1)(e)|SPE Operator|Mandatory|
|EHDSR-8|All SPE logs MUST be<br>kept at least for one<br>year|EHDS Art. 73(1)(e)|SPE Operator|Mandatory|
|EHDSR-9|<br>TOMs of SPEs MUST<br>be monitored for<br>securit|EHDS Art. 73(1)(f)|SPE Operator|Mandatory|
|EHDSR-10|y<br>EHD MUST be<br>identified in the data<br>permit|EHDS Art. 73(2)|HDAB|Mandatory|
|EHDSR-11|Health data holder<br>MUST upload the<br>permitted EHD to be<br>available in an SPE for<br>thehealthdata user|EHDS Art. 73(2)|Data Holder|Mandatory|
|EHDSR-12|Health data user MAY<br>download only non-<br>personal EHD from<br>SPE. Anonymised<br>personal data is non-<br>personal|EHDS Art. 73(2)|Data User|Mandatory|
|EHDSR-13|<br>HDAB MUST ensure<br>by reviewing that no<br>personal data is taken<br>out of the SPE by the<br>health data user|EHDS Art. 73(2)|HDAB|Mandatory|
|EHDSR-14|<br>Regular internal and<br>external security<br>audits MUST be done<br>onSPE TOMs|EHDS Art. 73(3)|SPE Operator|Mandatory|
|EHDSR-15|<br>SPE TOMs MUST<br>undergo risk<br>assessments|EHDS Art. 73(3)|SPE Operator|Mandatory|
|EHDSR-16|HDABs MUST ensure<br>that SPE TOMs audits<br>are carried out and<br>that risk assessments<br>leadtorisk mitigations|EHDS Art. 73(3)|HDAB|Mandatory|
|EHDSR-17|<br>When SPEs<br>mentioned in the EU|EHDS Art. 73(4)|SPE Operator|Mandatory|



32 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

||Data Act are used for<br>EHD, EHDS rules and<br>requirements MUST<br>befollowed||||
|---|---|---|---|---|
|EHDSR-18|SPEs MUST adapt to<br>TOMs that the<br>Commission will write<br>into EHDS<br>implementingacts|EHDS Art. 73(5)|SPE Operator|Mandatory|



**Figure 5.3.** SPE requirements derived from EHDS Article 73. Requirement identifiers follow the convention ‘EHDSR–n’, where ‘EHDS’ indicates the EHDS requirements namespace and ‘R’ denotes requirement. 



<!-- Start of picture text -->
EHDSR-1. HDAB MUSTusing<<Operational>> a datagrant permitaccess to EHD Oo EHDSR-7. All<<Functional>>SPEactorlogs MUST identify the o EHDSR-13.that no personalHDAB MUST<<Operational>> data Is takenensure outby of thereviewing SPEo<br>by the health data user<br>EHDSR-2. EHD<<Operational>> MUST be accessed using an D) ( EHDSR-8. All<<Operational>>SPE logs MUST be kept at leasto EHDSR-14. <<Operational>>Regular internal and external Oo<br>SPE for one year security audits MUST be done on SPE TOMs<br>EHDSR-3. Natural<<Functional>>persons listed in the dataOo EHDSR-9. TOMS<<Operational>>of SPEs MUST be monitoredo EHDSR-15. <<Operational>>SPE TOMs MUST undergo risk Oo<br>permit MAY access the identified EHD in SPE for security assessments<br>a<br>EHDSR-4, TOMs<<Functional>>MUST minimise the risk ofOo EHDSR-10. <<Operational>>EHD MUST be identified in the o EHDSR-16. <<Operational>>HDABs MUST ensure that SPE Do<br>unauthorised EHD access in SPEs data permit TOMs audits are carried out and that risk<br>assessments lead to risk mitigations<br>6 <<Functional>> o <<Operational>> o <<Operational>> o<br>EHDSR-S. Authorised health data users EHDSR-11. Health data holder MUST upload EHDSR-17. When SPEs mentioned in the EU<br>MUST be strongly identified the permittedfor theEHD healthto be dataavailable user in an SPE Data Actrequirementsare used  MUSTfor EHD, beEHDS followedrules and<br>6 <<Functional>> o <<Functional>> oO <<Operational>> ao<br>EHDSR-6. All access and operation logs of EHDSR~12. Health data user MAY download EHDSR-18. SPEs MUST adapt to TOMs that<br>SPE MUST be availableauditingfor verification and ‘Anonymisedonly non-personalpersonal dataEHDis fromnon-personalSPE. the Commissionimplementingwill writeactsinto EHDS<br><!-- End of picture text -->

Seven of these 18 requirements are functional in a way directly affecting the functionality of SPEs under EHDS (Figure 5.4). These requirements touch either security of data processing and user identity giving specific demands (SPER-1), or logging requirements (SPER-9) already covered in more general terms in generic SPE requirements. The problematics about logging details in EHDSR-6 already seen coming from the SPE definition is covered in chapter <u>Monitoring of SPE use</u> in Annex 7: Design considerations and expert commentary. 

**Figure 5.4.** EHDS SPE functional requirements. Requirement identifiers follow the convention: ‘SPER–n’ for general purpose SPE requirements (‘SPE’ namespace + ‘R’ for 

33 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

requirement) and ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for requirement). 



<!-- Start of picture text -->
/ ; SPE virtual (computer)requirementsenvironment minimum @ apermitEHDSR-3.MAY Naturalaccess personsthe identined listed inEHD thein dataSPE 57 ———--> aEHOSR-10, EHDdata MUST bepermit identified in the<br>sins exposing sense data<br>| SPER-4, SPE MUST provide adequate protection 5)-------><br>a users to unauthorised L------> GHDSR-S, Authorised Realth data users) EHDSR-4. TOMs MUST minimise the risk of 7<br>va MUST be strongly identified L..-.4 unauthorised EHD access in SPE<br>authorised users<br>c{ ‘SPER-S. SPE SHOULD promote collaboration among]<br>N<br>| SPER-6.“MUSTBetsolte Project-based omuser ech environments ter an opeof SPE See<br>Internet ‘only non-personal EHD from SPE.<br>: ‘Anonyinised personal data ls non-personal<br>ata they display<br>{ SPER-7, Authorised users MUST protect sensitive<br>SPER-8. Authorised users MUST interact with thelr<br>SPE project space onl through secure protocols<br>| 27<br>: ~~ EHOSR-7. All SPE ogs MUST identify the =><br>SPER-8, Hi actor<br>be logged and monitored ‘<br>{ All APIs connecting SPE components MUST) --—---»<br>~-+-=+->/EHDSR-6,SPE MUST be avaiableAllaccessauditingand foroperation logs verifcation andof &P<br><!-- End of picture text -->

### **5.4  Functional requirements for EHDS SPE** 

### **5.4.1  Export control** 

The only functional requirement that separates SPE under EHDS from generic SPE concept is its legal obligation to health data users to only export anonymised results (EHDSR-12). This topic will be discussed in chapter <u>Data export from SPE</u> of Annex 7: Design considerations and expert commentary. Export control is there further separated into three main areas affected: 

1. Export of anonymous results 

2. Returning of clinically significant results to the original data holders 

3. Creation of new datasets of enriched research data 

The anonymisation of results is further discussed in TEHDAS2 _D7.2 Guideline on data minimisation, pseudonymisation, anonymisation and synthetic data._ 

### **5.5  Operational requirements for EHDS SPE** 

**Context:** As previously explained, the goal of this deliverable is to support policy alignment, strategic planning, and high-level design of SPEs across Member States and stakeholders. As stipulated in Article 73 of the EHDS Regulation, the implementing acts will legally define the technical, organisational, information security, confidentiality, data protection, and interoperability requirements for SPEs. This chapter therefore delves into operational requirements to provide a robust basis for discussion and decision-making during the development and adoption of the EHDS implementing acts. That said, it is important to note that none of the requirements presented below are legally prescribed by this work. The exercise undertaken was to review established standards, certifications, directives, and best practices to formulate a list of recommended and mandatory operational requirements for 

34 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



SPEs. In the following sections, a list of recommendations is presented for key operational areas, including the suggested level of importance (mandatory or recommended) and the rationale for each requirement. This rationale may reference the conditions set in Article 73 of the EHDS Regulation and may also be complemented by guidance from other standards and frameworks relevant to information security, compliance, and operational management. 

Operational requirements in SPEs refer to the necessary processes, controls and capabilities that ensure systems handling sensitive data operate securely, reliably and in line with the functional obligations defined in Article 73 of the EHDS Regulation.  These requirements cover both technical and procedural aspects, such as access management, system configuration, monitoring, incident handling and service continuity. They are primarily derived from the functional requirements laid down in the EHDS Regulation, which establishes the mandatory framework for SPE setup and operation. 

However, it is important to consider that the EHDS Regulation enters a broader ecosystem of established standards, directives, and best practices that inform the design and implementation of operational controls. In developing the operational requirements presented in this section, we have analysed several state-of-the-art references to complement the EHDS provisions and provide practical guidance for SPE operators: 

- **ISO/IEC 27000 series**<sup>**6**</sup> :Internationally recognised standards for information security management, providing a structured approach for establishing, implementing, and maintaining an Information Security Management System (ISMS). While ISO 27001/27002 are not explicitly mandated by the EHDS Regulation, they offer widely accepted guidance for implementing robust security processes and controls. 

- **NIS2 Directive (Directive (EU) 2022/2555):** A European directive establishing cybersecurity risk management obligations. Importantly, NIS2 obligations may apply to SPE operators depending on their organisational context and national transposition. NIS2 provides guidance on areas such as incident response, access control, supply chain security, and business continuity. Its obligations serve as a reference for state-of-the-art operational practices, but compliance depends on the scope defined by national legislation. 

- **FitSM:** A practical framework for IT service management that supports structured service governance, clear role definitions, and disciplined operational processes. FitSM is not a mandatory requirement; rather it can be adapted to an organisation’s needs and resources. Implementation can be approached in phases, starting with core processes for operational stability, followed by scalability-focused processes, and culminating in continual improvement to enhance service performance and maturity. FitSM is proposed here as a helpful approach to unify governance and operational practices across SPE providers. 

- **General Data Protection Regulation (GDPR):** Establishes the legal framework for data protection and privacy of natural persons, including requirements for data processing accountability, security, confidentiality, and breach reporting. In the SPE context, GDPR provides crucial guidance for handling personal health data, defining principles for lawful 

6 ISO27001 https://www.iso.org/standard/27001 

35 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



processing, auditability, and data minimisation. Compliance with GDPR ensures that SPE operations protect the privacy rights of individuals while supporting lawful secondary use of health data. 

By drawing on these references, SPE operators can better understand the practices, protocols, and controls that support secure and resilient operation. Note that this report is **not intended to be a standalone implementation manual** . It does not prescribe specific products, detailed configurations, or deployment procedures, and it cannot by itself guarantee operational compliance or certification of SPEs. 

We will formulate SPE operational requirements under six categories (Figure 5.5): 

- Main SPE roles 

- SPE setup and access management 

- SPE auditing, compliance and reporting 

- Monitoring and incident management 

- Risk management and mitigation 

- Maintenance and support 

**Figure 5.5.** SPE operational requirement categories 



<!-- Start of picture text -->
SPE operational requirements a<br>Main SPE roles 7 SPE setup and £7 Auditing, 7<br>access ‘compliance and<br>management reporting<br>Monitoring and 7 Risk a Maintenance and/7<br>incident management support<br>management and mitigation<br><!-- End of picture text -->

We will mark these requirements in relation to the EHDS Regulation, its identified functional requirements, and to the four aforementioned regulations. 

#### **Main SPE roles** 

In the context of the EHDS, operational requirements are shaped by a framework of clearly defined roles that collectively ensure the secure, lawful, and ethical secondary use of electronic health data. 

The core roles - Health Data Access Body, SPE Operator, Data Holder, and Health Data User - each carry specific responsibilities that influence or depend on robust operational processes. These roles do not operate in isolation but rather in close interaction through structured processes, mutual dependencies and shared responsibilities that ensure compliance with legal standards, while also enabling technical interoperability and data protection. Their relation to EHDS SPE requirements is shown in Figure 5.6. 

**Figure 5.6.** The main SPE roles and their relation to identified EHDS SPE requirements. Purely functional requirements have been greyed down. Requirement identifiers follow the 

36 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

convention ‘EHDSR–n’, where ‘EHDS’ indicates the EHDS requirements namespace and ‘R’ denotes requirement. 



<!-- Start of picture text -->
a<br>a<br>ora —— — .<br>EHOSR-3. Natural persons listed in the data£7 eth= dite Coweal EXDSR-11.‘the permittedHealth EHD todatabe holderavailable MUSTin uploadan SPE 7<br>EHDSR-10, EHD MUST be identified in the £7 aac | == | rr“unauthorised EHD access in SPES oefor security<br>, e<br>say<br>‘TOMs[EHDSR-16.“assessmentsaudits HOABSare carriedMUST out andensure thatthat risk SPE’ ‘7 comener t > ‘BHDSR-6.‘SPE MUST beAll accessavailableand for operation verificationlogs and of C7 “EHOSR-15.SPE|cenaniel TOMs MUST undergo risk C7<br>lead to risk mitigations auditing<br>———— = aera<br>es<br>TO ee —_—_>————_<br>ca oa<br>‘EHOSR-12.eeHealth data us e r MAY download [7 lmplamentingacts<br>=e<br><!-- End of picture text -->

**HDAB:** The HDAB is the national authority designated under the EHDS Regulation to govern and oversee access to electronic health data for secondary use. In the context of SPEs, the HDAB plays a central regulatory and supervisory role to ensure that access to, processing of, and outputs derived from electronic health data comply with the conditions set out in the data permit and with applicable legal, security, and confidentiality requirements. In particular, the HDAB is responsible for ensuring that electronic health data made available by health data holders can be uploaded to, and accessed by health data users within a SPE, in the format and under the conditions specified in the data permit. The HDAB oversees that access within the SPE is limited to health data users and aligned with the approved purposes and safeguards defined in the permit. The HDAB is also responsible for reviewing electronic health data included in download requests from the SPE, in order to ensure that health data users are only able to extract non-personal electronic health data, including data in anonymised statistical form, in accordance with the EHDS Regulation and the conditions of the data permit. Furthermore, the HDAB must ensure that audits of SPEs are carried out on a regular basis, including audits performed by third parties. Where audits identify shortcomings, risks, or vulnerabilities in the SPE, the HDAB is required to ensure that appropriate corrective actions are taken. As part of its transparency obligations, each HDAB must publish a publicly available activity report every two years, including information on audits conducted on health data users and on the compliance of secure processing environments with the applicable standards, specifications, and requirements. Beyond these core regulatory responsibilities, HDABs may in practice act as a central repository of expertise on the secondary use of health data and serve as a primary point of contact for stakeholders. As a matter of good practice, HDABs may provide guidance on lawful and appropriate data use, deliver training on the handling of sensitive health data, and operate helpdesk or support functions to address enquiries related to data access, use, and compliance. These supporting activities, while not mandated by the EHDS Regulation, can contribute to consistent interpretation of requirements and to the effective and compliant use of secure processing environments. 

37 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**SPE Operator:** The SPE Operator refers to the organisational function responsible for the day-to-day operation, maintenance, and technical management of the SPE. While the EHDS Regulation does not explicitly define “SPE Operator” as a distinct legal role, this concept is introduced in this work to address the practical need for a clearly identified entity or function accountable for operating and maintaining the SPE in accordance with the requirements set out in Article 73 of the EHDS Regulation. In practice, the SPE Operator function may be fulfilled by the HDAB itself or by another organisation entrusted with operating the SPE. Regardless of the organisational setup, the allocation of tasks, responsibilities, and accountability related to SPE operations should be formally defined and documented to ensure clarity, traceability, and effective governance. The SPE Operator should be responsible for ensuring that the SPE operates securely, reliably, and continuously, that technical and organisational measures for access control, logging, monitoring, incident management, and service continuity are implemented and enforced, and that processing conditions defined in data permits, such as access restrictions, separation of processing contexts, and termination of processing upon permit expiry, are supported. Furthermore, the SPE Operator must ensure that the SPE remains compliant with applicable security, confidentiality, and data protection requirements relevant to its operation. It is important to note that, in the context of this work, the responsibilities of the SPE Operator are related and limited to the operation and management of the SPE itself and do not replace or override the regulatory responsibilities of the HDAB or the legal obligations of health data users. A clear separation and coordination of responsibilities between the SPE Operator, the HDAB, and health data users, including research leads, is essential to avoid ambiguity, duplication, or gaps in accountability. This work emphasises the importance of explicitly defining responsibility boundaries between the HDAB, the SPE Operator, and health data users, formally assigning and documenting operational responsibilities and delegated tasks related to SPE operation, and providing further guidance, at the implementation level, on governance models for establishing and operating SPEs, including scenarios where SPE services are provided by third parties. By introducing the SPE Operator as an operational role, this document aims to support clarity in responsibility allocation and to facilitate consistent implementation of the EHDS requirements across Member States, without prescribing a specific organisational or contractual model. 

**Data Holder:** The Data Holder is the organisation or entity that possesses the original health datasets, such as hospitals, research institutions or health registries. Health Data Holders are responsible for providing electronic health data in accordance with the conditions set out in the data permit and under appropriate legal, technical, and security safeguards. In the context of the SPEs, Health Data Holders make the requested data available for analysis within the SPE, ensuring that the data is provided in the format specified by the data permit and can be accessed securely by authorised health data users. 

**Health Data user:** The Health Data User is a natural or legal person, including Union institutions, bodies, offices, or agencies, that has been granted lawful access to electronic health data for secondary use pursuant to a data permit or a health data request approval. Health Data Users are authorised to access and process electronic health data only in accordance with the conditions set out in the data permit. When working within an SPE, Health Data Users must not provide access to the data, nor make it available, to any third party not explicitly listed in the data permit. Access rights are strictly tied to the authorised 

38 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



users identified in the data permit, ensuring that only those individuals can interact with the health data in the SPE. 

Health data user is here defined from the EHDS perspective as the entity that carries the responsibility for the approved health data. Natural persons mentioned in the health data permit are authorised users. For researchers, the situation is more complicated. To clarify it, we need to specify the correct **project context for their roles (** Figure 5.7). 

A **research project** may consist of many members with different roles, and not all of them are accessing sensitive data specified by the data permit. To get the data permit, the principal investigator (or one of the many) acts as the health data applicant to submit a data application. A positive decision creates the data permit that includes identifiers to approved **EHDS project** authorised users, of which the principal investigator is one. The data permit gives access to applied data and to at least one SPE service. Based on the data permit, the principal investigator establishes a project in the SPE to start analysing the data and includes other authorised users to it. 

**Figure 5.7** . Illustration of the use of the role name principal investigator in three different project contexts (work package ArchiMate elements). The principal investigators mean different things to the research group, the HDAB and SPE service. 



<!-- Start of picture text -->
Research project Qa<br>HDAB @EHDS project a)<br>Health data CD Health data CD<br>user applicant<br>Project adminCD Authorised CD Principal CD<br>user <@—__ investigator<br>§ ¥<br>Project Data permit &<br>member<br>i i; SPE project1+ o<br>sPEuser CD sPEuser CD Principal CD<br>———__— @—__imestigator<br>Principal CD<br>investigator<br>(Pl<br><!-- End of picture text -->

39 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



#### **SPE setup and access management** 

An SPE that is configured in accordance with the conditions set out in a data permit (Article 73, EHDSR-1). The data permit defines, among other elements, the purpose of processing (EHDSR-2), the data that will be accessed (EHDSR-10), the authorised health data users (EHDSR-3), and the specific SPE in which the processing is allowed. The Regulation further requires that SPEs be set up in a timely manner, so that HDABs are able to make health data available to the health data user within two months of receiving the data from the health data holder. This implies that the SPE must be operational within this timeframe and configured in line with the terms of the data permit. In addition, the Regulation requires that access to the SPE be restricted to authorised natural persons listed in the data permit, that appropriate technical and organisational measures be applied to prevent unauthorised access, and that the SPE be terminated after the expiry of the data permit, with the corresponding deletion or rendering unrecoverable of electronic health data within the legally defined timeframe. 

To give effect to these regulatory obligations, SPEs must rely on a set of core operational capabilities related to environment setup and access management. These include identity and access management mechanisms that ensure unique, auditable user identities, procedures for granting, modifying, and revoking access rights in line with data permit conditions, credential lifecycle management processes and controls for managing privileged access to the underlying infrastructure. In addition, SPE operators require service and configuration management practices that allow them to maintain an accurate overview of the services, systems, and components that form part of the SPE, and to ensure that each environment is configured and operated consistently with its authorised purpose. 

Defining operational requirements in this area presents several challenges. Access rights and system configurations are not static but are tightly coupled to administrative decisions taken by HDABs through data permits, which may change over time. SPE operators must therefore be able to reflect permit updates promptly and accurately in access controls and environment configurations. At the same time, the need to enforce strict access restrictions must be balanced with operational requirements for logging, auditability, incident response, and, where applicable, legal obligations related to traceability or scientific reproducibility. The termination and deletion of SPE environments after permit expiry further requires carefully designed procedures to ensure confidentiality and compliance, while allowing for exceptions mandated by applicable law. 

The operational requirements set out below provide a structured and practical basis for addressing these challenges. They describe recommended operational requirements for SPE setup and access management, indicating where requirements are considered mandatory or recommended, and explaining how they support compliance with the EHDS Regulation while enabling secure and effective operation of SPEs. 

Table 5.2. lists these requirements and their derivation that is shown in figure 5.8. 

**Figure 5.8.** SPE setup and access management. Requirement identifiers follow the convention: ‘SPER–n’ for general purpose SPE requirements (‘SPE’ namespace + ‘R’ for requirement), ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for 

40 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

requirement) and ‘OPR–n’ for operational requirements (‘OP’ namespace + ‘R’ for requirement). OP requirements and their importance are interpretations of the EHDS Regulation. 



<!-- Start of picture text -->
EHOSR-1. HOABUsingMUSTa datagrant permit.access to EHO 7 ==+ ‘SPE setup<<Mandatory>>and access management a o<br>it ‘OPR-1 . SPE Operator MUST have procedures in plac to enforce<br>i _________, eeei RE Ge uA user‘with authenticationthe data permitand associatedaccess restrictionswith the processingstrictly n accordanceof health<br>H data --------- 5027)<br>‘SPER-4, SPE MUST. |_........., [i[EHDSR-3.peememareccenNatural persons tiei) eelistedI inthe datat <7Be eesHi ‘OPR-2.managementThe SPE OperatorproceduresRippleMUSTcovering implementissuance, credentialmodification,fecycle a?<br>provide adequate i revocation, and periodic review<br>ection of credentials, n line wth<br>scsitounauthorsed semeaveagainst ae [EHOSR-S. Authorised health data users 7 HH ‘organisational securityaie policies and sk management Laine practices<br>users, -===-~">=-> MUST be strongly identified ae| |--L-s,0PR-3, SPE Operator MUST<<Mandatony>>limit the numberof authorised staffo<br>it<br>‘andany subcontractors who have high-prvleged acess<br>; EHDSR-4.-4, TOMs TOMs MUSTMUST minimiseminimise  thethe  riskrisk ofof 7)!i}| — -<<Recommended>>—— Dy--|----| 1}<br>oy a ae -— OPR-4. SPE OperatorIncludingSHOULDalmaintainservices a Service Portfolio r,t<br>(OPR-S. SPE Operator“<<Recommended>> SHOULD maintain a configuration a<br>managementoe data-base (CMDB) }e-------- SD<br>(0P8-6.‘the secureSPE processingOperator MUSTenvironment<<Mandatory>> implementupon mechanismsexpiration toofthe terminatedata ..|....-4<br>ema | ______, permitMedeetedAil electron or renderedhealthunrecoverabledata within thewithin environment sb months MUSTof<br>whilepermitensuring expiry, complianceincluding any backupswith applicable or redun-dantlegal obligations copes,and<br>‘waceabilty or reproducibly re-quirements where relevant.<br>Procedures MUST be formally documented, montored, and<br>aligned with risk assessments, confidentiality requirements and<br>‘applicable legal obligations<br><!-- End of picture text -->

**Table 5.2:** SPE setup and access management 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|**OPR-1**|EHDSR-1<br>EHDSR-3<br>EHDSR-4<br>EHDSR-5|Access<br>management|**SPE Operator MUST**<br>**have procedures in**<br>**place to enforce user**<br>**authentication and**<br>**access restrictions**<br>strictly in accordance<br>with**the data permit**<br>**associated with the**<br>**processing of health**<br>**data.**<br>These procedures shall<br>ensure that only<br>authorised natural<br>persons listed explicitly<br>in the data permit can<br>access the SPE. Access<br>rights shall be derived<br>from, limited to, and<br>continuously aligned<br>with the conditions of the<br>data permit, and shall be<br>reviewed and adjusted<br>as required to reflect<br>permit changes.<br>User identities shall be<br>unique, persistent,<br>auditable, and non-|Article 73(1)(a) -<br>Restriction of SPE<br>access to<br>authorised natural<br>persons listed in<br>the data permit<br>Article 73 (1)(d) -<br>Use of individual<br>and unique user<br>identities and<br>confidential access<br>modes to assure<br>health data users<br>have access only<br>to the electronic<br>health data<br>covered by their<br>data permit.<br>ISO/IEC 27001<br>and ISO/IEC<br>27002 - Best<br>practices on<br>authentication and<br>access control|Mandatory|



41 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||transferrable. Access<br>control mechanisms,<br>including role-based<br>access control, shall be<br>implemented to ensure<br>that users have only the<br>minimum level of access<br>necessary to perform<br>their authorised tasks<br>under the data permit.<br>Where the same natural<br>person is authorised<br>under multiple<br>concurrent data permits,<br>the SPE Operator MUST<br>ensure logical<br>separation of access<br>rights and processing<br>contexts per data permit,<br>in order to prevent<br>unauthorised cross-<br>access between permits.|||
|**OPR-2**|EHDSR-1<br>EHDSR-3<br>EHDSR-4<br>EHDSR-5||**The SPE Operator**<br>**MUST implement**<br>**credential lifecycle**<br>**management**<br>**procedures covering**<br>**issuance,**<br>**modification,**<br>**revocation, and**<br>**periodic review of**<br>**credentials, in line with**<br>**organisational security**<br>**policies and risk**<br>**management**<br>**practices.**<br>If an alias or user ID is<br>used, it must be<br>uniquely attributable to a<br>single individual within<br>the organisation's<br>identity management<br>system. The true identity<br>behind any alias must<br>be known and auditable<br>at all times.|ISO/IEC 27001<br>and ISO/IEC<br>27002 and<br>EHDSR principles<br>require secure<br>management of<br>credentials to<br>protect sensitive<br>health data,<br>ensuring<br>accountability and<br>traceability of all<br>actions within the<br>SPE. Proper<br>identity<br>management<br>prevents<br>unauthorised<br>access and<br>supports audit<br>readiness.|Mandatory|
|**OPR-3**|EHDSR-4|Access<br>management|**SPE Operator MUST**<br>**limit the number of**<br>**authorised staff and**<br>**any subcontractors**<br>**who have high-**<br>**privileged access**<br>**enabling them to**<br>**access or process**<br>**health data and MUST**<br>**implement effective**<br>**procedures for**<br>**managing and**<br>**monitoring such**|Article 73(1)(c) -<br>Restrict access to<br>electronic health<br>data in the SPE<br>(input, inspection,<br>modification, and<br>deletion) to a<br>limited number of<br>authorised and<br>identifiable<br>individuals.|Mandatory|



42 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||**access within the SPE**<br>**infrastructure.**<br>**Privileged access**<br>**rights shall be**<br>**reviewed at regular**<br>**intervals and**<br>**immediately revoked**<br>**when no longer**<br>**necessary.**<br>Exceptionally,<br>administrators may<br>obtain privileged access<br>for technical<br>troubleshooting or<br>incident response,<br>provided this is explicitly<br>authorised, time-limited,<br>and subject to enhanced<br>monitoring and<br>documentation.|ISO/IEC 27002<br>recommendation -<br>organisations must<br>strictly limit and<br>manage privileged<br>access by<br>assigning it only<br>when necessary,<br>regularly reviewing<br>permissions, and<br>logging all<br>privileged actions.<br>Elevated access<br>must be controlled:<br>authorised<br>temporarily,<br>detailed in logs,<br>and promptly<br>reviewed for<br>necessity and<br>accountability.||
|**OPR-4**||Set up|**SPE Operator SHOULD**<br>**maintain a Service**<br>**Portfolio including all**<br>**services**(e.g., data<br>ingestion, analysis<br>platforms, audit tools).<br>Include:<br>Descriptions<br>Availability<br>Security levels<br>Eligible user groups<br>(e.g., researchers, data<br>owners)<br>Publish the catalogue<br>internally and regularly<br>update it.|FitSM Service<br>Portfolio<br>recommendation|Recommended|
|**OPR-5**||Set up|**SPE Operator SHOULD**<br>**maintain a**<br>**configuration**<br>**management database**<br>**(CMDB)**that includes:<br>-<br>All virtual<br>machines, services,<br>APIs, and<br>databases<br>-<br>Tag systems based<br>on data<br>classification (e.g.,<br>sensitive,<br>anonymised)<br>The CMDB SHOULD be<br>kept up to date and<br>reflect the current<br>operational state of the<br>SPE.|FitSM<br>Configuration<br>Management<br>recommendation|Recommended|
|**OPR--6**|EHDSR-1|Set up|**SPE Operator MUST**<br>**implement**|Article 68(12) -<br>electronic health|Mandatory|



|D<br>|7.4 Technical, functional and security specifica<br>|tions of Secure Proce<br>|ssing Environments<br>43<br>|
|---|---|---|---|
|**#**<br>**Link**<br>|**Area**<br>**Requirement**<br>|**Rationale**<br>|**Importance**<br>|
||**mechanisms to**<br>**terminate the secure**<br>**processing**<br>**environment upon**<br>**expiration of the data**<br>**permit. All electronic**<br>**health data within the**<br>**environment MUST be**<br>**deleted or rendered**<br>**unrecoverable within**<br>**six months of permit**<br>**expiry, including any**<br>**backups or redundant**<br>**copies, while ensuring**<br>**compliance with**<br>**applicable legal**<br>**obligations and**<br>**traceability or**<br>**reproducibility**<br>**requirements where**<br>**relevant. Procedures**<br>**MUST be formally**<br>**documented,**<br>**monitored, and aligned**<br>**with risk assessments,**<br>**confidentiality**<br>**requirements and**<br>**applicable legal**<br>**obligations.**<br>|data in the SPE<br>must be deleted<br>within six months<br>of the data<br>permit’s expiry.<br>NIS2 emphasises<br>secure data<br>disposal as part of<br>business continuity<br>and disaster<br>recovery planning,<br>including<br>managing backups<br>and redundant<br>data to prevent<br>unauthorised<br>access or data<br>leaks.<br>Traceability,<br>reproducibility, and<br>other legal<br>obligations (AI Act,<br>Data Act) may<br>require certain<br>processed results<br>or outputs to be<br>retained in<br>accordance with<br>applicable laws.<br>The deletion and<br>retention policy<br>should balance<br>these obligations<br>with the mandate<br>to securely<br>terminate the SPE.<br>||
|**SPE auditing, co**<br>**Technical and or**<br>The EHDS Regu<br>mechanisms to en<br>particular, Article<br>organisational me<br>electronic health d<br>are required to en<br>third parties, and<br>through corrective<br>access to and act<br>processing operati|**mpliance and reporting**<br>**ganisational security measures**<br>lation establishes that SPEs<br>sure compliance with legal, org<br>73 requires that SPEs have<br>asures to minimise security risks<br>ata, and enable verification and au<br>sure that audits of SPEs are carr<br>that any identified shortcomings,<br>actions. The Regulation further re<br>ivities within the SPEs for the p<br>ons.|<br>must operate<br>anisational, and<br>in place app<br>, ensure confid<br>diting of proces<br>ied out on a re<br>risks, or vulne<br>quires the keep<br>eriod necessar<br>|under robust oversight<br>security obligations. In<br>ropriate technical and<br>entiality and integrity of<br>sing operations. HDABs<br>gular basis, including by<br>rabilities are addressed<br>ing of identifiable logs of<br>y to verify and audit all<br>|



44 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



To support these obligations in practice, SPEs require a coherent set of operational capabilities related to auditing, compliance, and reporting. These include mechanisms for conducting regular internal and external audits, processes for retaining and managing logs and access records that enable traceability of key activities and the maintenance of accurate and up-to-date documentation covering technical configurations, organisational procedures, and security controls. In addition, effective compliance relies on clearly assigned responsibilities, including dedicated and appropriately trained personnel who oversee adherence to legal, organisational, and technical obligations, act as points of contact for audits, and coordinate responses to identified risks or non-compliance. Structured management systems, such as information security and service management systems, further provide a systematic framework for implementing, monitoring, and continuously improving these controls, including supplier and change management practices. 

Defining operational requirements in this area also presents diverse challenges. Audit and compliance mechanisms must be risk-based and proportionate, considering the size, complexity, and risk profile of the SPE, while remaining sufficiently robust to meet regulatory expectations. Governance arrangements between HDABs, SPE operators, and other involved actors may differ across Member States and organisational contexts, requiring flexibility in how responsibilities are assigned and exercised. A particularly significant challenge lies in balancing operational feasibility with privacy and data protection considerations, especially with regard to logging and traceability. Logging practices must be detailed enough to enable effective audits and investigations, yet carefully designed to avoid excessive data collection, unnecessary intrusion into user activities, or the creation of unmanageable volumes of log data. Ensuring practical, proportionate, and privacy-respecting traceability is therefore a central consideration when defining operational controls in this domain. 

The operational requirements set out below provide a structured description of recommended practices for SPE auditing, compliance, and reporting. They specify mandatory and recommended requirements aimed at supporting compliance with the EHDS Regulation, while aligning with state-of-the-art standards and good practices for secure and accountable operation of SPEs. 

To ensure that health data is handled securely, SPEs must follow strict technical and organisational security measures. These measures help protect sensitive data, prevent unauthorised access, and comply with legal obligations under the EHDS Regulation and the NIS2 Directive. 

The EHDS Regulation, particularly Article 73, requires that SPEs minimise security risks, monitor compliance, and undergo regular audits to identify and fix vulnerabilities. At the same time, the NIS2 Directive sets additional cybersecurity rules, including risk assessments, encryption policies, incident response plans, and security checks for suppliers. 

One key requirement is that SPE Operators implement an ISMS to establish and maintain security policies aligned with applicable laws, such as the GDPR. The ISMS should also be complemented with backup and disaster recovery plans, employee cybersecurity training and use of encryption to protect data and security assessment of suppliers and external systems. By following these security measures, SPEs can provide a safe and reliable environment for processing health data while ensuring compliance with EU regulations. 

45 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

Table 5.3 lists these requirements and their derivation that is shown in Figure 5.9. 

**Figure 5.9.** SPE auditing, compliance and reporting. Requirement identifiers follow the convention: ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for requirement) and ‘OPR–n’ for operational requirements (‘OP’ namespace + ‘R’ for requirement). OP requirements and their importance are interpretations of the EHDS Regulation. 



<!-- Start of picture text -->
[HOSR-16, HOARs MUST ensure that SPE<br>( tstesament lead to rsk miigatons<br>H ‘Audnng, compliance and reporting o<br>eros write (D)___._secunty ‘EHOSR-14,audits14. RegularMUSTRegular  be mera!iteral doneandandon SPETOMSexternal extemal —7 -----------1----» ‘OPR-7. eEstiayauahsprotection,SPs MUSTto assess undergosedgeand operationalcompliance regular regu  internalrequirementstealwith security and exterand  ama,exaral 7= «ORK GD<br>0sTaide)arte |\ ‘HOSR-E/ Ai aces and Sprainops EID) "=ies Orn SPs MUST ncinlogrand<<<Mandatory>>cessreconi twenmre”)os.S| we1S<br>—is=--2  SPEMUST be avalabe for verifetonand "ty =~ ""va----» "Replyofall operations and enable audits or 5 eee<br>7 WN -<<dtandatory>> oO OE<br>i WON ‘OPR-9. The SPE operator MUST maintain up-to-date A PRE<br>\ \ A. ON | documentation af all relevant technical organisational and 41/178<br>\\ \\\\ ‘OPR-10. PE Operator<<Recommended>> SHOULD assign a Compliance OmheerIf/f | =O<br>H\ NY.h organisational‘designate responsibiiesandechnicalobigaionsto ensure adherenceapeabletathe to ep 0°Mii |iS<br>\ hh ‘operation ofthe SPE ) a<br>a|, HOSR-9, TOMSs of SPs MUST be monitored27 VN “<<Mandatory>> = ei<br>{or secur Lo--------'9 \. | ommeis. sre operator MUST have an operating information — | 7h. . /<br>\ i N <<<Recommended>> Win ra<br>\ H \ Management Sytem Fa aRe aos)<br>4 i \ sana mi; row<br>EHOSR-I5.SPETOMSMUST undergo isk £7) A. omt-13.5P€ operatorsImpact AssessmentsMUST conduct(OPAS)regularData Protecion ifj'/|i =n<br>"i <<Mandatory>> >» | #£<br>Ny.iN (OPR-14, SPE OperatorMUST maintain policiesto ensure i #<br>WaMN secur‘operation around procurementof systems, incuding systemsthe andmanagement development of and 4A 4<br>Wy suppier-related security rks: Such polices must equre ffs<br>WNSOS. Agreements‘appropiate with contractual secur andsafeguards ava causes(9. Oata where Processing appheable) |ie //<br>SN.i | Gnd“Inpanicalar aratcbasedon secry-relevantservcelevelsanderteal approach to monitoring supplies, focusing ff=, /<br>‘105 article [HOSR-I6,SPEs MUST adapt to TOM that \ ee‘pier s mi Li/i<br>736) -----> the Commissimplementingwill writeacts i nteon EHOS— -----------> S|\ gpp.as, spts‘th SHOULDimpactadopt and changesk Sesestmentmanagementprocess i!/<br>‘OPR-16. SPE Operator MUST<<Mandatory>>adopt release and deploymentoO<br>‘management process<br><!-- End of picture text -->

**Table 5.3:** SPE auditing, compliance and reporting 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|**OPR-7**|EHDSR-14|Auditing|**SPE**<br>**Operator**<br>**MUST**<br>**undergo regular internal**<br>**and**<br>**external**<br>**audits**<br>**to**<br>**assess**<br>**compliance**<br>**with**<br>**security, data protection,**|EHDS<br>Regulation<br>(Article<br>73(3))<br>explicitly requires regular audits by<br>internal or third-party entities.|Mandatory|



46 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||**and**<br>**operational**<br>**requirements.**<br>Audits must cover essential<br>aspects<br>including<br>risk<br>assessment,<br>planning,<br>execution, corrective actions,<br>and documentation, and must<br>be conducted in a risk-based<br>and proportionate manner,<br>considering the SPE’s size,<br>complexity, and risk profile.<br>Audit<br>arrangements,<br>including<br>scope<br>and<br>frequency, must be defined in<br>agreement with the relevant<br>HDAB.<br>At minimum:<br>• **Internal audits**shall include<br>a full audit of the SPE’s<br>ISMS<br>and<br>operational<br>controls at least once per<br>year.<br>Additional<br>internal<br>audits must be conducted<br>when significant changes<br>occur to the SPE’s services,<br>infrastructure, or risk profile<br>• **External audits**must be<br>conducted at least once<br>every three years.Additional<br>external audits must be carried<br>out<br>following<br>significant<br>structural or security-relevant<br>changes to the SPE, or after a<br>serious security incident.<br>Internal<br>audits<br>must<br>be<br>conducted<br>by<br>personnel<br>independent from the audited<br>activities, and external audits<br>must involve third parties with<br>appropriate competence or<br>accreditation.|NIS2<br>Directive<br>mandates<br>the<br>evaluation<br>of<br>risk-management<br>measures and corrective actions.<br>ISO/IEC 27001 and ISO/IEC 27002<br>require planned internal audits to verify<br>the ISMS and other controls. In<br>common<br>practice,<br>organisations<br>aligned with ISO/IEC 27001 conduct<br>internal<br>audits<br>at<br>least<br>annually.<br>External certification under ISO/IEC<br>27001 follows a three-year cycle, with a<br>full recertification audit every three<br>years.<br>To<br>maintain<br>certification,<br>accredited bodies conduct surveillance<br>audits at least once per year during the<br>first<br>and<br>second<br>years<br>of<br>the<br>certification cycle. These surveillance<br>audits are external, risk-based, and<br>narrower in scope than the three-year<br>recertification audit.<br>A risk-based and proportionate audit<br>approach, aligned with governance<br>arrangements agreed with the HDAB,<br>supports consistent implementation<br>across SPEs of different sizes and<br>complexity<br>while<br>ensuring<br>audit<br>independence,<br>accountability,<br>and<br>operational feasibility.||
|**OPR-8**|EHDSR-6|Auditing|**SPE Operator MUST retain**<br>**logs and access records to**<br>**ensure traceability of all**<br>**operations and enable**<br>**audits or investigations**<br>**when needed.**<br>The<br>logging<br>should<br>be<br>focused<br>on<br>key<br>actions,<br>including<br>data<br>access,<br>processing,<br>and<br>administrative activities, while<br>balancing<br>operational<br>feasibility<br>and<br>privacy<br>considerations.|EHDS Regulation (Article 73(1)(e))<br>obliges SPEs to ensure logs of data<br>access and operations/activities in the<br>SPE.<br>ISO/IEC 27002 defines how logs and<br>access records should be retained and<br>reviewed:<br>•<br>Logs should capture key details<br>such as user IDs, timestamps,<br>and the type of activity<br>performed. They must be<br>protected against tampering,<br>stored in a time-synchronised<br>environment, and regularly<br>reviewed to detect anomalies or|Mandatory|



47 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|||||unauthorised access. Logs<br>access should be restricted to<br>authorised personnel.<br>GDPR Article32(1)(b) requires<br>measures ensuring the ongoing<br>confidentiality, integrity, availability,<br>and resilience of processing systems,<br>for which audit trails are a key control.<br>Article 5(2) establishes the<br>accountability principle, requiring<br>controllers and processors to<br>demonstrate compliance with data<br>protection principles, which<br>operationally relies on reliable logs.<br>Article 30 requires records of<br>processing activities, which are<br>supported by structured logging of<br>system usage and access to personal<br>data.||
|**OPR-9**|EHDSR-14|Compliance/<br>Reporting|**SPE Operator MUST**<br>**maintain up-to-date**<br>**documentation of all**<br>**relevant technical,**<br>**organisational, and**<br>**security processes.**|ISO/IEC 27001 and ISO/IEC 27002<br>mandate control documentation and<br>maintenance of procedures and<br>records.<br>FitSM   supports structured<br>documentation as a basis for<br>consistent compliance and audit-<br>readiness.|Mandatory|
|**OPR-10**|EHDSR-14|Compliance|**SPE Operator SHOULD**<br>**assign a Compliance**<br>**Officer or designate**<br>**responsibilities to ensure**<br>**adherence to legal,**<br>**organisational, and**<br>**technical obligations**<br>**applicable to the operation**<br>**of the SPE.**This role may be<br>supported by other functions,<br>such as Privacy Officer or,<br>where applicable under the<br>GDPR, a DPO (Data<br>Protection Officer), and<br>servesas a point of contact<br>for audits, compliance, and<br>regulatory matters related to<br>SPE operations.|ISO/IEC 27002 recommends that roles<br>and responsibilities related to security<br>and compliance be clearly assigned<br>and communicated.<br>FitSM   recommends the assignment of<br>roles such as Information Security<br>Manager or Compliance Officer to<br>oversee governance. This ensures<br>accountability and provides a single<br>point of contact for audit, compliance,<br>and regulatory matters.|Recommended|
|**OPR-11**|EHDSR-15<br>EHDSR-16|Compliance|**SPE Operator MUST have**<br>**an operating information**<br>**security**<br>**management**<br>**system (ISMS)**in line with<br>the state of the art, for<br>example<br>following<br>the<br>requirements<br>of<br>ISO/IEC<br>27001.<br>Following<br>the<br>recommendations from the<br>FitSM   standard, this should<br>include:<br>- End-to-end encryption|To have an ISMS in place is already a<br>requirement of other laws (including<br>GDPR).<br>FitSM<br>-<br>Information<br>Security<br>Management requirement<br>ISO/IEC 27001 and ISO/IEC 27002<br>requirement|Mandatory|



48 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||- Role based access control<br>- Multifactor authentication<br>- Vulnerability<br>assessments<br>and penetration tracking<br>- Document<br>and<br>update<br>security controls|||
|**OPR-12**|EHDSR-14|Compliance|**SPE**<br>**Operator**<br>**SHOULD**<br>**establish**<br>**a**<br>**Service**<br>**Management**<br>**System**:<br>Define the scope of the SMS<br>to include all services and<br>components<br>involved<br>in<br>processing health data.<br>Appoint<br>a<br>Service<br>Management Officer (SMO)<br>responsible for maintaining<br>SMS compliance.|FitSM SMS requirement<br>ISO/IEC 27002: Maintain a real-time<br>inventory of assets used to process<br>health data|Recommended|
|**OPR-13**|EHDSR-14|Auditing|**SPE**<br>**Operator**<br>**MUST**<br>**conduct**<br>**regular**<br>**Data**<br>**Protection**<br>**Impact**<br>**Assessments (DPIAs)**|ISO/IEC 27002|Mandatory|
|**OPR-14**|EHDSR-14|Compliance|**SPE**<br>**Operator**<br>**MUST**<br>**maintain policies to ensure**<br>**security**<br>**around**<br>**procurement systems and**<br>**development and operation**<br>**of systems, including the**<br>**management of supplier-**<br>**related security risks. Such**<br>**policies**<br>**must**<br>**require**<br>**appropriate**<br>**contractual**<br>**safeguards**<br>**(e.g.**<br>**Data**<br>**Processing**<br>**Agreements**<br>**with security and audit**<br>**clauses where applicable)**<br>**and a risk-based approach**<br>**to**<br>**monitoring**<br>**suppliers,**<br>**focusing in particular on**<br>**security-relevant**<br>**service**<br>**levels**<br>**and**<br>**critical**<br>**suppliers.**|This is a NIS2 requirement to ensure<br>security around supply chains and the<br>relationship between the company and<br>the direct supplier. Companies must<br>choose security measures that fit the<br>vulnerabilities of each direct supplier.<br>And then companies must assess the<br>overall security level for all suppliers.<br>FitSM   requirements<br>-<br>Require<br>Data<br>Processing<br>Agreements<br>(DPAs)<br>with<br>security and audit clauses.<br>-<br>Monitor SLA compliance of<br>suppliers, particularly for<br>critical infrastructure<br>-<br>ISO/IEC 27002 – security clause within<br>procurement contracts|Mandatory|
||EHDSR-18|Compliance|SPE Operator MUST adapt to<br>TOMs that the Commission<br>will<br>write<br>into<br>EHDS<br>implementing acts.|Article 73(5)|Mandatory|
|**OPR-15**|EHDSR-15|TOM|**SPE**<br>**Operator**<br>**SHOULD**<br>**adopt change management**<br>**process with impact and**<br>**risk assessment**|FitSM   requirements|Recommended|
|**OPR-16**|EHDSR-15|TOM|**SPE Operator MUST adopt**<br>**a release and deployment**<br>**management**<br>**process.**<br>These may include staging<br>environments, rollback plans<br>and automated deployment<br>pipelines<br>(CI/CD).<br>The|FitSM<br>requires<br>that<br>changes<br>to<br>services and service components are<br>planned,<br>tested,<br>approved,<br>and<br>documented in order to minimise the<br>risk of service disruption and security<br>incidents.|Mandatory|



|<br>|D7.4 Technical, functional and security spe<br>|cifications of Secure Processing Environm<br>|ents<br>49<br>|
|---|---|---|---|
|**#**<br>**Link**<br>|**Area**<br>**Requirement**<br>|**Rationale**<br>|**Importance**<br>|
||release<br>and<br>deployment<br>process<br>MUST<br>include<br>controls to ensure software<br>integrity<br>and<br>secure<br>development<br>practices<br>throughout<br>the<br>software<br>lifecycle, including measures<br>such<br>as<br>controlled<br>code<br>changes, verification prior to<br>deployment, and prevention<br>of<br>unauthorised<br>or<br>unreviewed modifications to<br>production systems.<br>|ISO/IEC 27001 and ISO/IEC 27002<br>require<br>organisations<br>to<br>control<br>changes to information systems and to<br>ensure that software development,<br>release, and deployment processes<br>protect the confidentiality, integrity, and<br>availability of information assets. This<br>includes<br>safeguarding<br>software<br>integrity<br>and<br>preventing<br>the<br>introduction of vulnerabilities through<br>uncontrolled or insecure development<br>and deployment practices.<br>Given the sensitivity of electronic<br>health data processed within an SPE,<br>robust<br>release,<br>deployment,<br>and<br>secure development lifecycle controls<br>are necessary to reduce operational<br>and security risks and to support<br>compliance with EHDS requirements<br>for SPEs.<br>||
|**Monitoring a**<br>The EHDS R<br>and provide<br>establishes t<br>and processi<br>logs (Article<br>cases of mis<br>environment<br>form the lega<br>within SPEs.<br>To fulfil the<br>functionalitie<br>includes the<br>covering use<br>storage mec<br>and to ensur<br>clear inciden<br>authorities o<br>misuse. Effe<br>capability to<br>well as robu<br>data integrity|**nd incident management**<br>egulation requires that SPEs enable<br>mechanisms to detect, manage, a<br>hat SPEs must retain, for a minimu<br>ng of electronic health data, while e<br>73(1)(e)). The Regulation further i<br>use or security breaches, including<br>when necessary to protect data a<br>l basis for operational monitoring, i<br> <br>se requirements in practice, SP<br>s that support continuous monitorin<br>systematic recording and retention<br>r authentication, data access and m<br>hanisms are required to protect logs<br>e their availability for audits and inve<br>t reporting processes to notify HD<br>f security incidents or non-compli<br>ctive incident management further<br>promptly suspend or restrict access<br>st backup and disaster recovery pr<br>following an incident.|effective monitoring of proces<br>nd respond to security inciden<br>m of one-year, identifiable logs<br>nsuring confidentiality and inte<br>mplies the need for prompt in<br>the ability to restrict or halt<br>nd prevent further harm. Thes<br>ncident detection, and respons<br>Es must be equipped with<br>g and effective incident mana<br>of security- and compliance-<br>ovement, and administrative ac<br>against unauthorised access<br>stigations. In addition, SPEs m<br>ABs and, where applicable, o<br>ance findings, including data<br>requires the technical and o<br>and processing activities withi<br>ocedures to restore service av<br>|sing activities<br>ts. Article 73<br>of access to<br>grity of those<br>tervention in<br>access to the<br>e obligations<br>e capabilities<br>operational<br>gement. This<br>relevant logs,<br>tions. Secure<br>or tampering<br>ust establish<br>ther relevant<br>breaches or<br>rganisational<br>n the SPE, as<br>ailability and<br>|



50 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

Defining operational requirements in this area involves addressing several important challenges. A key consideration is ensuring that logging practices are proportionate, riskbased, and technically feasible. Excessive or overly detailed logging may be operationally burdensome, privacy-invasive, and disproportionate to the risk reduction achieved, while insufficient logging may undermine auditability and incident detection. Therefore, logs must be carefully scoped to capture information necessary for accountability and misuse detection, without collecting unnecessary detail on user behaviour. At the same time, logged information must be adequately protected against unauthorised access or manipulation. Incident reporting timelines and response procedures must also balance urgency with accuracy, ensuring timely notification without compromising the quality of incident analysis. These challenges have been explicitly taken into account in the formulation of the operational requirements below, which draw on established standards and best practices, including those reflected in ISO/IEC standards and incident reporting frameworks referenced in instruments such as the NIS2 Directive, to define proportionate, privacy-respecting, and operationally realistic requirements. 

The following operational requirements provide a structured description of recommended practices for monitoring and incident management in SPEs. They specify mandatory and recommended measures intended to support effective oversight, timely incident response, and resilient operation of SPEs in line with the EHDS Regulation. Table 5.4 lists these requirements and their derivation that is shown in Figure 5.10. 

**Figure 5.10.** Monitoring and incident management. Requirement identifiers follow the convention: ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for requirement) and ‘OPR–n’ for operational requirements (‘OP’ namespace + ‘R’ for requirement). OP requirements and their importance are interpretations of the EHDS Regulation. 



<!-- Start of picture text -->
Monitoring and incident management a<br>EHDSR-6. All access and operation logs of 7 aS oO<br>a--" - SPE MUST be availableen) for verification and --------» __QpR-17.‘identifiableSPElogsOperatorof securi-tyMUST recordand compliance= and retain | <=>==~~~=-~ en)<br>EHDS article (1) EHDSR-7. All SPE logs MUST identify the ----——-—-> relevantand activitiesaudit processingin the SPE, sufficientoperationsto verify<br>730Me) =>ao actor ‘OPR-18.<<Mandatory>> oa<br>EHDSR-8, All SPE logs MUST be kept at least 7)______._ mechanismSPEsto retain MUST logs implement of user accessa secure tostorage the SPE<br>for one year T fora minimum period of one year<br>EHDS>| article (1) EHDSR-9. TOMs ofSPEs MUST be monitored (7 CR irate<<Mandatory>>CSao ‘so27%K<br>Cry 7777-7" security incidents oF non-compliance findings =<br>including data breaches or misuse ,<br>EHDSR-15. SPE TOMs MUST undergo risk 27 “a -<<Recommended>>¥ o Aa<br>HDS738) article ()----> assessments Y“ALe ‘OPR-20.reportingGefined SPE timelinesincidents Operatorto SHOULDforthecommunicatingHDA: adoptEarly and warning and enforce ff“i“i<br>~~~» ‘TOMsEHDSR-16. audits areHDABs carried MUST ensureout and thatthat risk SPE? -------- notifeation:Detailed incidentwithinnotification:24 hours ofwithin incident72 hoursdetection. of veff<br>‘assessments lead to risk mitigations tendon, incidentthandetection. one monthFinal aftrincident the incidentreport:no later!”Ye<br>‘J <<Mandatory>> D ft a)<br>K OPR-21. SPE Operator MUST be able to promptly <=}-------~<br>Shalt aceess and processing activities within the SPE<br>\.,_when misuse or data breaches<br>ao<br>(OPR-22. SPE Operator<<Mandatory>>MUST haveare disas-teridentified ===<br>recovery procedures in place to restore the<br>availabilty and integrity of the SPE services,<br>including critical system com-ponents,<br>configurations, and platform-level functionality,<br>from clean backups, and to resume normal service<br>‘opera-tions following an incident<br><!-- End of picture text -->

51 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Table 5.4:** Detailed operational requirements for monitoring and incident management 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|**OPR-17**|EHDSR-6<br>EHDSR-7|Monitoring|**SPE Operator MUST record**<br>**and retain identifiable logs of**<br>**security and compliance-**<br>**relevant activities in the SPE,**<br>**sufficient to verify and audit**<br>**processing operations.**<br>**Logging must, at a minimum,**<br>**cover:**<br>•**User authentication and**<br>**access to electronic health**<br>**data**<br>•**Data import, export, or**<br>**release of outputs**<br>•**Administrative actions**<br>**affecting access rights or**<br>**data availability.**<br>Logging MUST be proportionate,<br>risk-based, and technically<br>feasible, and MUST avoid<br>unnecessary collection of<br>detailed user behaviour not<br>required for auditability or misuse<br>detection. Logged information<br>MUST be protected against<br>unauthorised access or<br>tampering and retained for the<br>period necessary to support<br>audits and investigations in<br>accordance with applicable law.|Article 73(1)(e) - the keeping<br>of identifiable logs of access<br>to and activities in the secure<br>processing environment for<br>the period necessary to verify<br>and audit all processing<br>operations in that<br>environment.<br>Proportionate, risk-based<br>logging of security- and<br>compliance-relevant events is<br>consistent with recognised<br>information security practices<br>and avoids unnecessary<br>operational burden,<br>excessive data generation, or<br>privacy risks.<br>FitSM guidance recommends<br>that recommends that track<br>incidents and requests<br>should be logged using ITSM<br>tools (e.g., Jira Service<br>Management, Freshservice),<br>classify and prioritise events<br>based on data sensitivity and<br>service impact, provide a<br>clear user-facing incident<br>reporting process, and<br>maintain a 24/7 on-call rota<br>for critical service issues.<br>These practices support<br>effective incident handling<br>and oversight without<br>prescribing specific technical<br>implementations.|Mandatory|
|**OPR-18**|EHDSR-8|Monitoring|**SPE Operator MUST implement**<br>**a secure storage process to**<br>**retain logs of user access to**<br>**the SPE for a minimum period**<br>**of one** **year**. Log storage must<br>ensure integrity, confidentiality,<br>and protection against<br>unauthorised access or<br>tampering. While one year is the<br>minimum retention period, longer<br>retention (5 years) is<br>recommended to support<br>effective auditing procedures.|Article 73(1)(e) - logs of<br>access shall be kept for at<br>least one year|Mandatory|
|**OPR-19**|EHDSR-9<br>EHDSR-16|Incident<br>management|**A reporting process MUST be**<br>**in place to notify HDABs and**<br>**relevant authorities of security**<br>**incidents or non-compliance**<br>**findings including data**<br>**breaches or misuse. The**<br>**reporting process must define**<br>**reporting responsibilities,**<br>**notification timelines,**|EHDS Regulation (Art. 73(3))<br>requires that SPEs allow for<br>compliance checks and audits<br>by competent authorities to<br>notify the HDAB of any<br>incidents<br>affecting<br>the<br>integrity or confidentiality of<br>data.|Mandatory|



52 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||**escalation paths, and required**<br>**documentation**|ISO/IEC 27002 requirement:<br>Incident reporting procedures<br>should define what must be<br>reported,<br>by<br>whom,<br>how<br>quickly, and through which<br>communication<br>channels.<br>This includes the escalation<br>path,<br>responsibilities,<br>and<br>necessary documentation to<br>ensure timely and effective<br>response.||
|**OPR-20**|EHDSR-16|Incident<br>management|**SPE Operator SHOULD adopt**<br>**and enforce defined timelines**<br>**for communicating and**<br>**reporting incidents to the**<br>**relevant HDAB(s):**<br>•  Early warning notification:<br>within 24 hours of incident<br>detection<br>• Detailed incident notification:<br>within 72 hours of incident<br>detection<br>• Final incident report: no later<br>than one month after the<br>incident<br>Incident reports must include<br>minimum fields such as incident<br>ID, timestamp, severity, affected<br>data, and mitigation actions.|The NIS2 Directive mandates<br>incident notification to the<br>relevant authorities within 24<br>hours of awareness, with a<br>more<br>detailed<br>incident<br>notification to be submitted<br>within 72 hours (or within 24<br>hours for certain entities, such<br>as trusted service providers).<br>Additionally, a final incident<br>report must be provided no<br>later than one month after the<br>incident.|Recommended|
|**OPR-21**|EHDSR-16|Incident<br>Management|**SPE Operator MUST be able to**<br>**promptly halt access and**<br>**processing activities within the**<br>**SPE when misuse or data**<br>**breaches are identified.**|Article 73(3) - HDABs shall<br>take corrective action for any<br>shortcomings, risks or<br>vulnerabilities identified.<br>ISO 27001 and ISO/IEC<br>27002 and NIS2<br>requirements identify the<br>need for organisations to<br>have procedures to stop or<br>restrict access and<br>processing in response to<br>security incidents or data<br>breaches.|Mandatory|
|**OPR-22**|EHDSR-16|Incident<br>management|**SPE Operator MUST have**<br>**disaster recovery procedures**<br>**in place to restore the**<br>**availability and integrity of the**<br>**SPE services, including critical**<br>**system components,**<br>**configurations, and platform-**<br>**level functionality, from clean**<br>**backups, and to resume**<br>**normal service operations**<br>**following an incident.**<br>Project-specific data recovery<br>may be limited to what is feasible<br>within backup and retention<br>policies. Disaster recovery<br>measures should be<br>proportionate to the SPE’s size,|ISO 27001 and ISO/IEC<br>27002 - Organisations must<br>have a disaster recovery<br>process that includes<br>restoring systems and<br>service functionality from<br>backups and return to normal<br>operations.<br>NIS2 requirement -<br>Organisations must have<br>plans for business continuity<br>and disaster recovery,<br>including the ability to restore<br>critical systems and services<br>after an incident.|Mandatory|



53 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**<br>**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|
|||complexity, risk profile, and<br>service criticality.|||



#### **Risk management and mitigation** 

Risk management and mitigation are fundamental to ensuring the security, reliability, and resilience of SPEs. The EHDS Regulation establishes clear obligations for this purpose: Article 73(1)(b) requires that technical and organisational measures are in place to minimise the risk of unauthorised reading, copying, modification, or removal of electronic health data hosted in the SPE. Beyond the regulatory requirements, proactive risk management and mitigation represent core functionalities of secure information systems, providing a structured approach to identifying, assessing, and addressing potential threats to system operations, data confidentiality, and user compliance. Based on the identified threats to SPEs (see Annex 10: Classification of risks and threats against SPEs for examples), the associated risks can be assessed and appropriate mitigation strategies planned. By implementing a comprehensive risk management framework, SPE providers can protect sensitive data and maintain system integrity. 

To implement effective risk management in SPEs, a combination of technical, organisational, and operational functionalities is required. These include robust security measures, such as firewalls, encryption, intrusion detection systems, and controlled access mechanisms, to prevent unauthorised access or manipulation of sensitive data. Personnel interacting with the SPE, including HDAB staff, SPE operator staff, and health data users, must receive role-specific training covering EHDS compliance, secure data handling, and relevant GDPR principles. Operational measures must also incorporate strategies for backup management, disaster recovery, and crisis management to ensure business continuity and resilience in case of incidents. Complementary operational practices, such as service-level agreements (SLAs) and regular restoration of backups, support preparedness and accountability across the entire SPE workflow. 

Defining operational requirements for risk management and mitigation involves addressing several important considerations. Effective risk mitigation requires coordination across all actors involved in the data provision and processing workflow, from the HDAB to the SPE operator and down to health data users. Additionally, preparedness for recovery and incident response is critical in a live processing environment, where ongoing data analysis must be safeguarded against loss, disruption, or compromise. Effective measures must therefore ensure that work-in-progress analyses can continue safely while maintaining protection of data integrity and confidentiality. These considerations have guided the formulation of the operational requirements outlined below. 

The following operational requirements provide a structured description of recommended practices for risk management and mitigation in SPEs. They specify mandatory and recommended measures designed to safeguard sensitive data, maintain system integrity, and ensure continuity of SPE operations in line with the EHDS Regulation. 

54 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

Table 5.5. lists additional requirements and their derivation that is shown in Figure 5.11. 

**Figure 5.11.** Risk management and mitigation. Requirement identifiers follow the convention: ‘SPER–n’ for general purpose SPE requirements (‘SPE’ namespace + ‘R’ for requirement), ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for requirement) and ‘OPR–n’ for operational requirements (‘OP’ namespace + ‘R’ for requirement). OP requirements and their importance are interpretations of the EHDS Regulation. 



<!-- Start of picture text -->
Ask management<br>and mivgston a<br>105 ance (9) BIOSR-4. TOMS MUST minimise the risk of C7 protect data,(0Pn-23. Se includingoperator theMUST<citandaton>> ute adoptof firewallbustenryptonecurty measures and itusionto a<br>7aANo) p> unauthorised EHD accessim SPES =—- Geecontmaiteaton systems or orderremovalto preventof seratve unauthorisedinformation acess,<br><<Mandatory> n<br>brotectSPER-6, senstveAuthorid usesdata they MUSTdisplay C7 -------> BisGRIN) ace) -----1=--% (Pn-24,streetsEHDS complianceMOAB deta,staffrequirements, and role-speiie SPC Operator health formation al> who intrator wang withthe covering SPE”),2)’. | sor<br>secuntyreceteeauvaletbest racestraning coming pronerom DPR.databy teHe h a  responaielthndlingatain ers the HOAB, SPEanshou d << -~-3----~\\<br>HOS7a)» article ) TonsEHDSR-16.ees audi HOABsare earedee MUSTee ensureout and  thatthat SPEak 7)= OPR-25.Covering theImanagementThe  minimumSPE providerduaterSoevohons<<ttandaton>>necenar MUSTrecovery. a implement aspects oftheand SP.cts tostrategies ensuemanagement seat for backup and a= *--------~\aLS ws? o<br>(078-26.<<Mandatory>> ao é<br>proceduresThe Se provider MUST Implement ybersecuty /<br>management measuresto regulary an evaluate promotthe fundamental efecveness cyberscurty of rik //<br>Dractces and prone necessary raning. /<br>guaranees,response/resltonStAs,0rn-27, suchSP Operator‘<<Recommended>>SHOULDtines defineforLascientsthat nce inde time secrtyDi;“= 7-== == rsw<br>ab data encryption guarantees, inden response mes,<br>ind ad oging /<br>a<br>(0F8-28.DlatormScves,Thea partSPensuringOperatorof standard<tecommended>>preparednessSHOULD texture regular developmenfor nentestore sndesponsebackup operonsothe fs<br><!-- End of picture text -->

**Table 5.5:** Risk management and mitigation 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|**OPR-23**|EHDSR-16|Risk<br>mitigation|**SPE**<br>**Operator**<br>**MUST**<br>**adopt**<br>**robust security measures to**<br>**protect data, including the use of**<br>**firewalls,**<br>**encryption,**<br>**and**<br>**intrusion detection systems, to**<br>**prevent unauthorised access,**<br>**modification,**<br>**or**<br>**removal**<br>**of**<br>**sensitive information.**|Article 73(1)(b) - Technical and<br>organisational measures must be in<br>place to minimise the risk of the<br>unauthorised reading, copying,<br>modification or removal of EHD<br>hosted in the SPE.<br>NIS2 Directive explicitly references the<br>implementation of appropriate security<br>measures, such as incident detection<br>and regular security assessments, to<br>protect data and systems. Measures<br>like<br>encryption<br>and<br>multi-factor<br>authentication are considered state-<br>of-the-art practices that can support<br>compliance with these requirements.|Mandatory|
|**OPR-24**|EHDSR-16|Risk<br>mitigation|**HDAB staff and SPE Operator**<br>**staff who interact with the SPE**|Article 68(1)(e) - The health data<br>applicant must demonstrate sufficient|Mandatory|



55 

|ba<br>|<br><br><br>|D7.4<br><br>|Technical, functional and security spec<br><br>|ifications of Secure Processing Environ<br><br>|ments<br>55<br><br>|
|---|---|---|---|---|---|
|**#**<br>|**Link**<br>|**Area**<br>|**Requirement**<br>|**Rationale**<br>|**Importance**<br>|
|||~~y~~|**MUST receive detailed, role-**<br>**specific information or training**<br>**covering EHDS compliance**<br>**requirements, health data**<br>**handling in the SPE and**<br>**security best practices coming**<br>**from GDPR. Health data users**<br>**should receive equivalent**<br>**training provided by the**<br>**responsible HDAB, covering the**<br>**minimum necessary aspects to**<br>**ensure secure and compliant**<br>**use of the SPE.**<br>~~E~~|technical and organisational<br>measures to prevent data misuse and<br>protect the rights of data holders and<br>individuals.<br>Article 73(1)(b) - Technical and<br>organisational measures must be in<br>place to minimise the risk of the<br>unauthorised reading, copying,<br>modification or removal of EHD<br>hosted in the SPE.<br>ISO 27001 and ISO/IEC 27002<br>require role-appropriate security<br>training for all staff and relevant<br>contractors, covering policies,<br>responsibilities, and basic security<br>practices.<br>||
|**OPR-25**<br>|EHDSR-16<br>|Risk<br>mitigation<br>|**The SPE Operator MUST**<br>**implement strategies for backup**<br>**management, disaster recovery,**<br>**and crisis management.**<br>|NIS2<br>directive<br>stipulates<br>that<br>organisations should have a plan for<br>managing business operations during<br>and after a security incident. This<br>means that backups must be up to<br>date. There must also be a plan for<br>ensuring access to IT systems and<br>their operating functions during and<br>after a security incident.<br>|Mandatory<br>|
|**OPR-26**<br>|EHDSR-16<br>|Risk<br>mitigation<br>|**The SPE Operator MUST**<br>**implement cybersecurity**<br>**procedures to regularly**<br>**evaluate the effectiveness of**<br>**risk-management measures and**<br>**promote fundamental**<br>**cybersecurity practices and**<br>**provide necessary training.**<br>~~t~~<br>|NIS2<br>directive<br>requires<br>that<br>employees<br>receive<br>cybersecurity<br>training<br>and<br>practice<br>for<br>basic<br>computer hygiene.<br>~~t~~<br>|Mandatory<br>|
|**OPR-27**<br><br>|EHDSR-16<br><br>|Risk<br>mitigation<br><br>|**SPE Operator SHOULD define**<br>**SLAs that include uptime**<br>**guarantees, response/resolution**<br>**times for incidents include**<br>**security SLAs, such as data**<br>**encryption guarantees, incident**<br>**response times, and audit**<br>**logging.**<br><br><br>~~i~~<br>|FitSM   Service Level Management<br>recommendation – a service<br>catalogue must be maintained, and<br>SLAs should clearly define service<br>targets such as uptime, response<br>times, and resolution times.<br><br><br>~~f~~<br>|Recommended<br><br><br>~~e~~|
|**OPR-28**<br><br>|EHDSR-16<br><br>|Risk<br>mitigation<br><br>|**The SPE Operator SHOULD**<br>**regularly restore backups to the**<br>**platform as part of standard**<br>**feature development and**<br>**operational activities, ensuring**<br>**preparedness for incident**<br>**response.**<br><br><br><br>~~f~~|NIS2 directive - organisations should<br>have a plan for managing business<br>operations during and after a security<br>incident. This means that backups<br>must be up to date. There must also<br>be a plan for ensuring access to IT<br>systems and their operating functions<br>during and after a security incident.<br><br> <br>~~t~~<br>~~t~~|Recommended<br><br><br><br>~~|~~|



56 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



#### **Maintenance and support** 

Maintenance and support mechanisms are essential to ensure that SPEs remain secure, reliable, and fully operational over time. While the EHDS Regulation does not explicitly define detailed operational requirements for these activities, Article 73(3) establishes that corrective actions must be taken for any shortcomings, risks, or vulnerabilities identified during audits of SPEs. Furthermore, the regulation implies that SPEs must be resilient and ensure service continuity, which necessitates responsive support and structured maintenance processes. Beyond regulatory obligations, maintenance and support are fundamental practices in information systems management, providing the mechanisms to manage updates, resolve incidents, and preserve operational integrity while sustaining user confidence. 

To achieve effective maintenance and support in SPEs, several high-level functionalities are needed. These include robust patch management and system update processes to promptly identify, test, and deploy security patches, updates to operating systems, firmware, and application software, and controlled change management procedures to ensure that updates do not compromise ongoing analyses or system stability. Dedicated technical support with clearly defined SLAs and escalation paths is required to assist users and address operational issues promptly. Support staff must be trained in information security, privacy procedures, and specific SPE operational practices. Additionally, maintaining a knowledge base and support documentation helps streamline issue resolution, reduces response times, and mitigates the risk of user errors or repeated support requests. 

Defining operational requirements for maintenance and support involves careful consideration of several challenges. SPEs must balance the need to keep systems up-todate and secure with the need to preserve reproducibility, operational continuity, and compliance with active data permits. Changes, updates, or patches can have unintended consequences on ongoing analyses, so a controlled change management process is essential to assess backward compatibility, identify potential risks, and coordinate updates with all relevant stakeholders. Furthermore, as SPEs will be new systems used by multiple actors, clear support structures, comprehensive documentation, and accessible guidance are critical to prevent overloading technical support teams and to ensure smooth onboarding and user adoption. These considerations underpin the operational requirements elaborated below, providing guidance to maintain SPE functionality, reliability, and regulatory compliance. 

The following operational requirements provide a structured description of recommended practices for maintenance and support in SPEs, focusing on system updates, patch management, change control, and user assistance to ensure resilient and secure operation. Table 5.6 lists these requirements and their derivation that is shown in Figure 5.12. 

**Figure 5.12.** Maintenance and support. Requirement identifiers follow the convention: ‘EHDSR–n’ for EHDS requirements (‘EHDS’ namespace + ‘R’ for requirement) and ‘OPR– 

57 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

n’ for operational requirements (‘OP’ namespace + ‘R’ for requirement). OP requirements and their importance are interpretations of the EHDS Regulation. 



<!-- Start of picture text -->
Maintenance and support a<br>(0PR-29. The SPE oper<<M a torndatory>>MUST implement a<br>patch management policy to identify, evaluate, a formaland apply<br>Security patches in a timely manner based on severity<br>/OPR-30.f <<Mandatory>> DB) | ----------<br>/ ensure timelySPEs MUST and secure establish updates a system update of sofware, process OS,and.  to g—--2024-|S. uD)<br>¥ firmware, tested prior to deployment =<br>/e <<Recommended>> r= ie<br>Le (0PR-31.<br>Me used for assessingA change themanagementimpact of patchesprocess SHOULDand updates be ‘ eeeAK,<br>‘eH0S artice EHDSR-16. HOABS MUST ensure that SPE 7 # beforeincluding appivingan assessmenthem t o ofthebackwardproductioncompat blity env i ronment,and aia,wae soz<br>733) ~--> TOMS audits are carried out and that risk | ---------> potential effects on ongoing data permit projects, in. <-———~2{°--$------~<br>assessments lead to risk mitigations ‘order to preserve reproducibility and operational aX;<br>AN <<Mandatory>> eae<br>\ ‘OPR-32. SPEs MUST provide dedicated technical support Vee<br>a with clearly defined SLAS and escalation paths for ee<br>Bs addressing incidents and technical issues [| ~—vhvoT,<br>\ <<Mandatory>> a / %<br>‘ (OPR-33. SPE suppor staff MUST be trained in 4 row)<br>\, information security and privacy procedures, with roles <“—740~~=~======-=~<br>\ ‘and responsibilities clearly defined ey i<br>‘OPR-34. A knowledge<<Recommended>>base and support documentation ao<br>SHOULD be maintained to assist in common issue<br>‘resolution and improve incident response times<br><!-- End of picture text -->

**Table 5.6:** Maintenance and support 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
|**OPR-29**|EHDSR-16|Maintenance|**The SPE Operator MUST**<br>**implement a formal patch**<br>**management policy to**<br>**identify, evaluate, and**<br>**apply security patches in a**<br>**timely manner based on**<br>**severity.**|EHDS Regulation (Article 73(3)<br>requires corrective actions for any<br>shortcomings, risks or vulnerabilities<br>identified un the process of SPE<br>audits.<br>NIS2<br>Directive<br>mandates<br>organisations to implement risk<br>management measures that include<br>updating systems to protect against<br>known vulnerabilities.<br>ISO/IEC 27001 and ISO/IEC 27002<br>explicitly<br>require<br>a<br>patch<br>management process.|Mandatory|
|**OPR-30**|EHDSR-16|Maintenance|**SPE Operator MUST**<br>**establish a system update**<br>**process to ensure timely**<br>**and secure updates of**<br>**software, OS, and**<br>**firmware, tested prior to**<br>**deployment.**|NIS2 Directive stipulates regular<br>system maintenance and software<br>updates to reduce risk exposure.<br>ISO/IEC 27001 and ISO/IEC 27002<br>require that information systems are<br>regularly updated with new versions<br>and<br>patches.<br>FitSM   requirement - structured<br>and traceable system update<br>processes must be in place|Mandatory|
|**OPR-31**|EHDSR-16|Maintenance|**A change management**<br>**process SHOULD be used**<br>**for assessing the impact of**<br>**patches and updates**|ISO/IEC 27001 and ISO/IEC 27002<br>requirements recommend that<br>changes to information systems are<br>controlled and authorised to avoid|Recommended|



58 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**#**|**Link**|**Area**|**Requirement**|**Rationale**|**Importance**|
|---|---|---|---|---|---|
||||**before applying them to**<br>**the production**<br>**environment, including an**<br>**assessment of backward**<br>**compatibility and potential**<br>**effects on ongoing data**<br>**permit projects, in order to**<br>**preserve reproducibility**<br>**and operational continuity.**|disruptions or vulnerabilities.<br>FitSM   requirement - all changes to<br>services or infrastructure must be<br>reviewed, approved, and<br>documented, ensuring continuity<br>and stability during patching and<br>updates. This reduces the risk of<br>unplanned outages or system<br>compromise.||
|**OPR-32**|EHDSR-16|Support|**SPE Operator MUST**<br>**provide dedicated**<br>**technical support with**<br>**clearly defined SLAs and**<br>**escalation paths for**<br>**addressing incidents and**<br>**technical issues.**|EHDS Regulation (Article 73(3))<br>requires SPEs to be resilient and<br>ensure service continuity, implying<br>that support services must be<br>available and responsive.<br>NIS2 Directive: Need for incident<br>handling and response capabilities.<br>ISO/IEC 27001 and ISO/IEC 27002<br>requires that technical support be<br>available to ensure effective<br>incident detection, response, and<br>recovery.|Mandatory|
|**OPR-33**|EHDSR-16|Support|**SPE Operator support staff**<br>**MUST be trained in**<br>**information security and**<br>**privacy procedures, with**<br>**roles and responsibilities**<br>**clearly defined.**|ISO/IEC 27002 highlights the<br>importance of assigning roles and<br>responsibilities related to security<br>and ensuring adequate training.<br>NIS2 Directive requires that<br>personnel involved in system<br>operation receive regular<br>cybersecurity awareness training.<br>FitSM   requirement**-**ongoing<br>education and role-based training<br>should be provided to ensure staff<br>can respond effectively to incidents<br>and manage secure systems.|Mandatory|
|**OPR-34**|EHDSR-16|Support|**A knowledge base and**<br>**support documentation**<br>**SHOULD be maintained to**<br>**assist in common issue**<br>**resolution and improve**<br>**incident response times.**|ISO/IEC 27002 - Documentation of<br>known issues and responses shall<br>be kept to improve incident<br>handling and system stability**.**<br>FitSM   requirement - Building and<br>maintaining a knowledge base as<br>part of support operations to enable<br>faster resolution and avoid<br>repetition of known problems. This<br>contributes to efficiency and<br>organisational learning in support<br>environments.|Recommended|



59 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **5.6  Technical interoperability requirements** 

#### **General** 

Existing EHDS technical requirements (Specific Contract no.22 documents: D02.03 Requirements Catalogue<sup>7</sup> , D03.03 Architecture Artefacts<sup>8</sup> , D03.03 System Specifications<sup>9</sup> ) are not directly addressing technical interoperability, but we have aligned with these documents where applicable, adopting consistent terminology and using the architecture described in them as a reference for interoperability requirements. 

The high-level technical architecture of the EHDS SPE is depicted in Figure 5.13.  Interfaces towards the following entities are identified: 

- Data user applications 

- Data holder applications 

- External SPEs 

- HDAB coordinator portal 

This section provides high-level technical specifications for the data user and data holder application interfaces as well as the interface for connecting external SPEs. The specifications are applicable both for federated computing and traditional data processing. The governance and safeguarding processes needed for setting up and managing the interfaces are beyond the scope of this deliverable. 

> 7 D02.03 Requirements Catalogue for Scale-Up version. Specific Contract no. 22 under Framework Contract SLG.AVT.DI07926 - BEACON – Lot2, Date: 17.12.2024, Version 3.1. 

> 8 D03.03 Architecture Artefacts – Scale-Up version. Specific Contract no. 22 under Framework Contract DI7925-DI7932 – BEACON – Lot2: Analysis and design of the European Health Data Space infrastructure for secondary use of health data (HealthData@EU), Date: 4.12.2024, Version 1.0. 

> 9 D03.03 System specifications – Scale-Up version. Specific Contract no. 22 under Framework Contract DI7925-DI7932 – BEACON – Lot2: Analysis and design of the European Health Data Space infrastructure for secondary use of health data (HealthData@EU), Date: 10.12.2024, Version 1.0. 

60 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 5.13.** High-level technical architecture of EHDS SPE (modified from D03.03 Architecture Artefacts). 



<!-- Start of picture text -->
Secure Processing Environment fas}<br>Control and B45, Project workspace FY<br>management<br>Data Fa] Remote ro” q<br>— pera 1D intestace [7<br>User wv =" Data user<br>ser Auth. application<br>‘Gent Dat a Deertea<br>bat anata APlservice2 user |) “apiuser ><br>coord.Hoasportal €]—— Actvity Ea] librariestoolsan<br>monitoring Fa o PEO spe<br>g) monitoringCompliance | ——— SPEservice +> endpointservice —————_ endpointservice<br>Access<br>Control<br>Access i St pO 2)<br>restriction DataholderAPI service 1 oara >, Dataapplication holder<br><!-- End of picture text -->

Data user application is a user-facing interface supported by the SPE infrastructure. It allows users to securely connect to their designated project workspace, which is isolated from the other workspaces. Two technical approaches should be supported by the SPE: (1) remote desktop connection and 2) API based connection. 

**The remote desktop (RD) interface** allows the data user to interactively process data in the project workspace. Remote desktop is the legacy approach widely used in the currently existing SPE installations. The data user application (remote desktop client) allows the user to access the project workspace as if working directly on its host machine, supporting interactive tasks such as file management, software execution, and visualisation. 

**The API interface** enables more versatile user applications, such as web portals and standalone applications provided or authorised by the HDAB. The API based data user application may enable to trigger execution of functions (e.g. data processing scripts), monitor progress of function execution, retrieve anonymous data analysis results, download anonymised data sets, communicate with authorised organisation (HDAB, authorised participant) and upload custom tools, supporting contents (e.g. vocabularies) and additional data sets. The API interface also is a prerequisite for federated analysis as outlined in Section 4.2.2. 

The SPE operator is responsible for setting up the required processes and controls to ensure that the exposed API services ensure privacy protection and compliance with EHDS Regulations.  For instance, it should be possible for the SPE operator to manually or automatically verify that the downloaded contents meet anonymity requirements. 

61 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Data holder application** is the data holder’s interface supported by the SPE infrastructure. The application enables the data holder to upload data to the SPE based on an accepted data permit. The data holder application uses an API based connection mechanism. 

**SPE service endpoint** enables connections to external SPEs. Such connections enable federated networks of trusted SPEs to be formed. Options for setting up such networks are discussed in the <u>SPE federation</u> chapter. 

HDAB coordinator portal connection enables the relevant organisation (HDAB, authorised participant or SPE operator) user to carry out overall management of the SPE and to execute specific tasks needed to support data usage and ensure regulatory compliance. Technical specifications for connecting the HDAB coordinator portal with SPEs may vary between implementations and are not in the scope of this deliverable. 

To fulfil the regulatory requirements (EHDS, Article 73) the SPE operator shall provide the RD interface and the data holder API shown in Figure 5.13.  Implementation of the data user API and SPE service endpoint is recommended, but not obligatory. 

Technical requirements for the interfaces are listed in the following subsections. 

#### **Scope** 

The following are **out of scope** for this deliverable: 

- Implications for EHDS governance, such as the authorisation of data transfers between SPEs and the deployment or execution of required software components (see also SPE federation) 

- Manual implementation of federated analysis, for example, cases where the user manually combines results from separate analyses, as permitted by their approved data permit(s). 

### **5.6.1  Data user and data holder API requirements** 

Technical interoperability requirements of federated SPE under EHDS Regulation have the namespace acronym ‘TI’ for **Technical Interoperability** followed by the letter ‘R’. TI requirements do not fall under EHDS Regulation. Importance levels of its requirements are valid only within its namespace. 

**Table 5.7:** General API requirements 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-1|**Client application.**The API services MUST be accessed via<br>data user and data holder applications, which can be<br>dedicated client applications or browser-based applications.|Mandatory|
|TIR-2|**Architectural style.**The API MUST follow a web services<br>architecture (e.g., RESTful, GraphQL), enabling stateless<br>request/response interactions and supporting secure file trans-<br>fer protocols. The implementation MUST adhere to common|Mandatory|



|<br>|D7.4 Technical, functional and security specifications of Secure Processing<br>|Environments<br>62<br>|
|---|---|---|
||architectural and security practices, including resource<br>grouping and, where appropriate, the use of microservices to<br>isolate sensitive services.<br>||
|TIR-3<br>|**Communication protocol.**The API MUST use industry-<br>standard security protocols to en-sure compatibility with<br>standard web clients and server implementations. For API<br>requests, HTTPS MUST be supported, and for file operations,<br>secure file transfer protocols such as HTTPS, SFTP, or FTPS<br>MUST be supported, where applicable.<br>|Mandatory<br>|
|TIR-4<br>|<br>**Data exchange format.**The API MUST support industry-<br>standard data formats, ensuring at least JSON is available for<br>requests and responses, while allowing additional formats as<br>needed.<br>|Mandatory<br>|
|TIR-5<br>|**File transfers.**The API MUST be capable of uploading and<br>downloading files using stand-ard file types (e.g. CSV and<br>parquet). It MUST provide configurable restrictions on allowed<br>file types and transfer directions (upload/download) separately<br>for each API and workspace. For large files, the API MUST<br>support efficient handling, including resumable transfers,<br>asynchronous processing where appropriate, and configurable<br>timeout settings to accom-modate long-duration operations.<br>|Mandatory<br>|
|TIR-6<br>**Table 5.8:**<br>**#**<br><br>|<br>**API documentation.**The API MUST provide clear, machine-<br>readable documentation (e.g., OpenAPI/Swagger) in<br>accordance with ISO 27001 information security and change<br>management controls to ensure proper governance,<br>traceability, and compliance.<br> API security and access control requirements<br>**Requirement**<br><br>|Mandatory<br>**Importance**<br><br>|
|TIR-7<br>|**Authentication and authorisation.**All requests to data user<br>and data holder API functions MUST be authenticated and<br>authorised using industry-standard methods (e.g., OpenID<br>Connect, OAuth 2.1 with JWT, API keys, and JWS-signed<br>requests). The access control mechanism MUST enforce<br>attribute-based access control (ABAC), limiting access based<br>on attributes such as user role, organisation, clearance level,<br>and data permit approval sta-tus.<br>|Mandatory<br>|
|TIR-8<br>|<br>**Data encryption.**The API MUST ensure data in transit is<br>encrypted using industry-standard protocols (e.g., TLS). For<br>added security, the API MUST support content encryption<br>(e.g., AES-256) prior to transmission, enforced by the HDAB,<br>to protect data even if stored by the API. When encryption is<br>applied, encryption keys MUST be managed and stored<br>securely in accordance with industry best practices, such as<br>via a dedicated key management system (KMS)<br>|Mandatory<br>|
|TIR-9<br>|.<br>**Input validation and sanitisation.**The API MUST validate<br>and sanitise all incoming data using industry-standard<br>practices to prevent injection attacks (e.g., SQLi, XSS) and<br>mal-formed requests. Encrypted payloads MUST be decrypted<br>before validation, and only pre-defined, approved request<br>types are allowed to be processed.<br>|Mandatory<br>|



63 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|TIR-10|**Error handling and security.**Error responses MUST avoid<br>exposing sensitive details (e.g., stack traces, internal error<br>codes) while providing meaningful messages for debug-ging.|Mandatory|
|---|---|---|
|TIR-11|**Network access control.**API access MAY be restricted<br>based on network-level controls, including firewall rules, IP<br>whitelisting, or Virtual Private Network (VPN) restrictions.|Recommended|



**Table 5.9:** API service management and monitoring 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-12|**Logging and auditing.**The API MUST log all requests,<br>responses, and errors following industry-standard practices to<br>support monitoring and compliance. Logging MUST adhere to<br>a predefined purpose and retention period, ensuring that data<br>is kept only as long as necessary and in accordance with<br>applicable policies.|Mandatory|
|TIR-13|**Monitoring and alerts.**The API MUST monitor usage,<br>failures, performance metrics, and service availability in<br>accordance with industry-standard practices, and alerts MUST<br>be generated for any detected anomalies to support<br>operational reliability and compliance.|Mandatory|
|TIR-14|**API version management.**The API MUST have<br>mechanisms to approve, deploy, and retire API versions,<br>following industry-standard practices and aligning with ISO<br>27001 change management controls to ensure secure and<br>controlled updates.|Mandatory|



**Table 5.10:** API performance and scalability 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-15|**Response time.**The API SHOULD meet defined latency and<br>response time SLAs.|Recommended|
|TIR-16|**Load handling.**The system SHOULD handle expected and<br>peak loads efficiently, with rate limiting and throttling<br>mechanisms in place if necessary.|Recommended|
|TIR-17|**Data Validity.**The API SHOULD ensure that payloads of<br>requests and responses comply with the specified data<br>formats and content standards, applying appropriate semantic<br>valida-tion mechanisms. This ensures consistency, accuracy,<br>and interoperability of exchanged data, preventing the delivery<br>of erroneous or inconsistent content.|Recommended|



### **5.6.2  Data user remote desktop interface** 

**Table 5.11:** General remote desktop interface requirements 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-18|**Functionality.**The remote desktop interface MUST enable|Mandatory|
||the data user to interactively access and process data with a||



64 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

||remote desktop application (“SPE UI” in D03.03 Architecture<br>Artefacts).||
|---|---|---|
|TIR-19|**Data user application.**The data user MUST be able to use<br>a standard browser or a dedicated client to access the remote<br>desktop environment.|Mandatory|
|TIR-20|**Platform compatibility.**The remote desktop solution MUST<br>support remote desk-top clients running on standard operating<br>systems including (e.g., Windows, macOS, Linux).|Mandatory|
|TIR-21|**Protocol support.**The remote desktop solution MUST use<br>industry-standard, purpose-built remote access protocols<br>(e.g., RDP or VNC) to establish connections between the<br>client and server. All communication MUST be encrypted in<br>transit using industry-standard secure protocols. If SSH is<br>used, it SHALL be restricted to transport or tunneling purposes<br>only and SHALL NOT provide interactive shell or file transfer<br>access to end users.|Mandatory|



**Table 5.12:** Remote desktop security and access control 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-22|**Authentication and authorisation.**Access to the remote<br>desktop interface MUST require multifactor authentication<br>(MFA) in accordance with industry-standard security practices.<br>The system MUST enforce attribute-based access control<br>(ABAC), limiting access based on attributes such as user role,<br>organisation, clearance level, and data permit approval sta-<br>tus, ensuring that only authorised users can access the<br>system.|Mandatory|
|TIR-23|**Network Access Control.**Access MAY be restricted based<br>on network-level controls, including firewall rules, IP<br>whitelisting, or VPN restrictions|Recommended|
|TIR-24|**Session management.**Idle sessions MUST be automatically<br>terminated after a predefined time to prevent unauthorised<br>access. Users MUST be logged out or locked after a period of<br>inactivity.|Mandatory|
|TIR-25|**Data transfer restrictions.**Clipboard sharing and file<br>transfers MUST be restricted by default to prevent<br>unauthorised export of data from the SPE. Changes to or<br>removal of these restrictions MUST be configurable at the<br>discretion of the HDAB.|Mandatory|



**Table 5.13:** Remote desktop service management and monitoring 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-26|**Logging and auditing.**All remote sessions MUST be logged<br>in accordance with industry-standard practices, including<br>authentication attempts, connection times, and actions per-<br>formed during the session. Logging MUST adhere to a<br>predefined purpose and retention period, ensuring that data is<br>kept only as long as necessary and in accordance with<br>applicable policies.|Mandatory|



65 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|TIR-27|**Monitoring and alerts.**Service usage, failures, performance|Mandatory|
|---|---|---|
||metrics and service availability MUST be monitored, with||
||alerts for anomalies.||



### **5.6.3  SPE service endpoint** 

**Table 5.14:** General SPE service endpoint requirements 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-28|**Functionality.**The service endpoint MAY enable<br>communication between trusted SPEs.|Recommended|
|TIR-29|**Communication Protocol.**The interface MUST support<br>protocols required for client-server and bidirectional streaming<br>communication (e.g., gRPC with HTTP/2 or an equivalent). All<br>such connections MUST use industry-standard secure<br>protocols (e.g., TLS) to protect data in transit.|Mandatory|



**Table 5.15:** SPE service endpoint security and access control 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-30|**Authentication and authorisation.**All connections MUST be<br>authenticated using industry-standard mechanisms (e.g.,<br>mutual TLS (mTLS) or token-based authentication), and all<br>data MUST be transmitted over industry-standard secure<br>channels to ensure confidentiality and integrity.|Mandatory|
|TIR-31|**Client whitelisting.**Connecting clients MUST be preapproved<br>before establishing a connection.|Mandatory|
|TIR-32|**Network access control.**The interface MAY be configured<br>to restrict access using firewall rules, IP whitelisting, VPN<br>access, other network-level policies and holistic approaches<br>such as virtual closed networks.|Recommended|



**Table 5.16:** SPE service endpoint service management and monitoring 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-33|**Logging and auditing.**All connection sessions MUST be<br>logged in accordance with indus-try-standard practices,<br>including requests, responses, streaming events and<br>connection times. Logging MUST adhere to a predefined<br>purpose and retention period, ensuring that da-ta is kept only<br>as long as necessary and in accordance with applicable<br>policies.|Mandatory|
|TIR-34|**Monitoring and alerts.**Real-time monitoring of streaming<br>sessions, errors, latency, and security threats MUST be<br>implemented. Alerts MUST be generated based on anomalous<br>activity (e.g., failed authentication attempts, unusual data<br>patterns).|Mandatory|



66 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Table 5.17:** SPE service endpoint performance and scalability 

|**#**|**Requirement**|**Importance**|
|---|---|---|
|TIR-35|**Response time and streaming performance.**The interface<br>MUST meet defined latency and response time SLAs.|Mandatory|
|TIR-36|**Load handling.**The system MUST implement flow control to<br>manage varying loads and prevent overloads, using rate<br>limiting, throttling, and adaptive resource allocation as needed.|Mandatory|



### **5.6.4  Relation to existing specifications** 

Existing specifications (D03.03 Architecture Artefacts) use the term “SPE UI”, which seems to refer to a remote desktop type interface used in legacy SPE implementations.  In this deliverable, we have proposed two types of data user applications: (1) the legacy remote desktop approach and (2) a new approach where the data user application interacts with the SPE via a web API interface. Approach (1) provides a familiar, typically browser-based, method for data users. Approach (2) enables new ways to enable more efficient ways to exchange information between the health data user and the SPE environment, including the possibility to execute federated analysis in multiple SPEs. 

Similarly, we propose the API approach to be used also for the data holder application, where such approach would enable a more efficient process with less manual interaction needed. 

We have included the interface for connecting external SPEs, which is not covered in D03.03 Architecture Artefacts. This interface enables advanced federated learning scenarios requiring direct information exchange between SPEs. These scenarios need careful governance and implementation to comply with EHDS Regulation which are not in the scope of this deliverable.  The development of more detailed specifications for the API and the SPE service point, together with the associated governance models, shall be key objectives of subsequent development activities. 

### **5.7  Challenges for EHDS SPE** 

### **5.7.1  Operational requirements for EHDS SPE federation** 

The paragraphs of Article 73 of the EHDS Regulation contain very specific legal demands for SPEs that function primarily in isolation. We have interpreted these to form 18 practical requirements out of them (See chapter EHDS SPE requirements and <u>Annex 9: EHDS article 73 analysis to deduce SPE requirements). Many of them are purely operational, meaning</u> their successful and secure application depend on the interplay of the personnel maintaining the services and the processes they implement, rather than being purely technical. Extending these requirements to fully support federated processing within EHDS, these requirements need to be interpreted and deployed in a uniform manner throughout the federation to maintain the functioning and security of services. 

In addition to EHDS, the catch-all security standards applied to high-end security services and organisations are the ISO/IEC 27000 -family of standards (ISO 27K) where ISO/IEC 27002 deals with information security controls. These are not very helpful for determining 

67 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



specific technical requirements for SPEs that go beyond it. The bulk of ISO27K requirements are operational, affecting the organisation maintaining the service. 

The NIS2 Directive builds on ISO 27K security demands and requires reporting within member countries and collection of all serious incidents to an EU-wide registry. 

We have organised and tabulated various operational demands to the SPE from EHDS, ISO 27K and NIS2 (see <u>Operational EHDS SPE requirements), but have excluded operational</u> requirements that direct HDAB and its reporting requirements to the EU central platform. 

Our evaluation also includes the FitSM standard, which we suggest as a lightweight framework to support cohesion of operation and reporting for EHDS-compliant SPEs because we feel it offers significant advantages to the EHDS over ISO 27K that is closed, heavyweight and expensive to certify against. 

FitSM is a lightweight, open-source standard for IT Service Management, developed through an EC funded project (FedSM, 2012-2015) and still actively maintained today. It supports any service delivery scenario but is unusual in supporting federated service provision and being much easier to implement in academic and public sector than other heavier traditional frameworks. FitSM has a wider scope than ISO 27K but covers information security management and can be easily integrated with an ISO27K management system. It offers strong advantages in that it can then connect security requirements more thoroughly to service design and delivery, service level management, capacity and availability management, customer relationship management and other IT Service Management processes (e.g. Service Portfolio Management, Incident & Problem Management, Change Management, Service Level Management). 

The core FitSM documentation is freely available under a Creative Commons licence, so it can be easily embedded and referenced in organisational and national documentation. This lets it be used as a free and lightweight reference model for managing services and for connecting security and operational requirements across EHDS. 

FitSM is proposed here as a practical framework to support coordination and documentation but does not replace the legal obligations established under the EHDS Regulation or related EU legislation. 

To ensure mutual trust across the EHDS SPEs, the documentation produced by each MS should demonstrate that auditing processes are implemented consistently and meet the common safeguards required under Article 73. This documentation should enable Member States to recognise each other's SPEs as compliant with the Regulation. Without such transparency and alignment, the SPE federation cannot guarantee a uniform level of protection for sensitive data across borders, thereby undermining its core objective 

FitSM should offer a lightweight and cost-effective way for EHDS SPE federation to coordinate its operational requirements to fulfil that goal. 

We recommend that EHDS should build its guidance for EHDS SPE federation compliance reporting based on FitSM. 

68 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **5.7.2  Cybersecurity of SPE infrastructure** 

This chapter of the SPE security considerations deals with challenges arising from virtualisation that are wider than SPE, e.g. the 18 security functions of the CIS framework<sup>10</sup> . 

SPE implementation is typically run as part of a virtualisation service where the aim is to isolate the user's project environment from other user environments and fully control the access to additional services. This isolation is built using nested security structures, where user applications run within virtualised environments that simulate their own operating systems, hosted on a local network. Eventually, the virtualisation layers interface with the physical hardware, where all processes are ultimately executed. 

The main aim of cybersecurity guidelines is to determine what is the adequate protection for a given setup balancing both enabling and limiting aspects. Given the aim to tap into creativity of researchers, we have already highlighted the need for openness and information sharing among the project members that requires them to understand their responsibilities and implications of their actions because too onerous technical actions are counterproductive. 

In our minimum requirements for SPEs these are expressed by **SPER-4** and **SPER-6** . We may rephrase these sentiments to: SPE isolation measures SHOULD protect everything else except user’s own immediate environment. Unfortunate users of an SPE should be allowed to find themselves in a situation where they exercise their freedom of actions to the extent that they lose the most recent results and their environment must be recreated to re-allow them access to the permitted sensitive data. 

Following the same logic, it should not matter what applications users have access to or what they have installed themselves. The operating system setup should prevent the harm from spreading outside the immediate user environment. If the users or their applications gain elevated access privileges, the network isolation is there for the next layer of protection. They should never reach administrative control of the system. 

However, it is not elephants all the way down. Networks and processes run on physical hardware. Secure processing running on the hardware maintained by the SPE service provider is seen as private cloud. In contrast, services running on public cloud necessarily involve trust to the cloud provider. 

The figure 5.14 illustrates the nested structure of computer cybersecurity layers and the full chain of trust inside a private cloud should enable the provider to control the operating system layer and offer its users SPE as a Platform as a Service (PaaS) where users have wide freedoms to import and install their own software. If services are built on public cloud, SPE operator might not have enough trust to the underlying services to provide high enough security, so they might have to restrict user’s abilities to install software. Then SPE is essentially providing Software as a Service (SaaS). 

10 CIS Controls https://www.cisecurity.org/controls/cis-controls-list 

69 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Figure 5.14.** Nested isolation of SPE processing. 



<!-- Start of picture text -->
SPE virtual (computer) environment isolation 6<br>Physical isolation 8<br>Network isolation lm}<br>Operating system isolation im] Platform as a F Private cloud<br>Service (PaaS) <@&———<br>Programme FE} Software as a<br>isolation Service (SaaS) Trusted &<br>> | public cloud<br>Public cloud FE)<br><!-- End of picture text -->

A key outcome of the UK community-driven SATRE project is a standard architecture specification for TREs (See <u>Annex 8: SATRE). Closely aligned with TEHDAS2, it defines</u> core TRE capabilities and criteria for assessing compliance. Regarding network security and nested isolation, the SATRE specifications include the following mandatory requirement: SATRE 2.2.9. “Your TRE must control and manage all of its network infrastructure”. However, globally available public cloud services are common use in UK. 

The recent proliferation of public clouds is based on reliance on laws and regulations providing foundations for usual business subcontracts that have been seen enough to elevate public clouds to the same level as private clouds. 

Public cloud providers may be subject to extraterritorial legislation (e.g. US CLOUD Act<sup>11</sup> ). The suitability of such providers for SPE hosting must therefore be reassessed under EU data protection, cybersecurity, and sovereignty requirements. The recent American governmental policy shift to emphasise US presidential prerogative power has already led to calls for purely European cyber infrastructure to safeguarding sensitive European data<sup>12</sup> . 

The current political climate has made it clear that cybersecurity requirements for SPEs and their federation will need to be reconsidered to redefine the adequate level of trust for sensitive data computer infrastructure is run on. 

### **5.7.3  Projection to EHDS SPE Federation** 

Secondary use in EHDS is a federation of interconnected services sharing information about available health data, as detailed in the EHDS Regulation. It provides legal requirements for 

> 11 CLOUD Act https://en.wikipedia.org/wiki/CLOUD_Act 12 e.g. EuroStack https://euro-stack.eu/ 

70 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



member states to produce metadata of their health datasets and requires those to be findable centrally though the HealthData@EU infrastructure. 

EHDS has a legal obligation for moving sensitive data only within jurisdiction, demanding at least one SPE service for processing the permitted data in each member country and one for the European Commission. The latter will primarily serve European Union’s institutions, bodies, offices and agencies (Article 75(2)). Additionally, the member state EHDS official, HDAB, may allow their data to be processed alone or in together with other permitted datasets in any of the approved European SPEs. 

Moreover, EHDS calls other European infrastructures like ERICs and EDICs Authorised Participant (AP) (Article 75(4)) that may participate in the HealthData@EU.  EHDS data permits will then allow users to access the data based on the legal framework of that AP and get access to the data in the EHDS 73 compliant SPE provided by that AP. 

The initial design of EHDS was based on the assumption of a stand-alone SPE maintained by HDAB. Data transfer would have been solely within each jurisdiction and would not need to be included into EHDS. However, the need to combine datasets over national borders and especially the rise of federated computing (see Federated computing) makes it necessary to bridge the gap from stand-alone SPE that works under one organisation by defining general requirements of an SPE federation. 

EHDS is already an SPE federation in almost all but in name and technical support. The defined general SPE federation requirements are regardless of federation structure (Figure 4.7). Their main limitations arise from sensitivity of data. They enable sensitive data processing beyond a single service to cover processing over multiple separate but linked services within one organisation (like database or HPC), as well as enabling processing over organisational borders. These requirements should work for _ad hoc_ proprietary data as well as EHDS-based processing. 

Federation rules will need to direct the collaboration and establish federation services for management, mutual trust, findability and information sharing. An SPE federation will need findability services to locate datasets and SPEs. EHDS already includes detailed instructions for data findability services, but a similar approach will be needed to SPEs, too, depending on the national setting. Heath data users will need to search and compare a catalogue to find EHDS compliant SPEs nationally across EU. 

### **5.7.4  Data access management and SPE interoperability** 

This section outlines the key requirements for interoperable and secure data access in an SPE federation, with emphasis on automation, standardisation, and support for scalable cross-border secondary use of health data under the EHDS Regulation. 

The interoperability and scalability of an SPE federation largely depends on the efficiency of data access management. The security of large-scale dataset management needs automated procedures that manual data management cannot match. It has been estimated that to reach similar throughput of data permits in the future European EHDS framework serving the whole EU as the Findata authority did manually in 2024 for Finland, would need European member states altogether hire 10000 persons to handle all the applications (Jaakko Leinonen, CSC, FI, personal communication). 

71 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

The lack of scalability in manual management of sensitive data life cycles (see <u>Annex 6: Sensitive data lifecycles) has been the driver for designing the automated "state-of-art"</u> approaches (see <u>Annex 7: Scenarios). It is also the reason why this report defining the</u> requirements and capabilities of SPE has been unable to do it without considering all the sensitive data lifecycle components. They are totally interdependent on each other. Enabling better functionality in one will not be possible without the other components supporting that. 

The core functionality of the SPE is to process sensitive data. We already have a good grasp on how it can be done securely and ample approaches to make it happen more efficiently (see <u>Annex 7: Scenarios), but they all depend on the capabilities of other components of the</u> federation. 

Cornerstones of this scalable infrastructure are: 

- Shared identity and authorisation 

- Machine-actionable access permits 

- Data streaming 

- Structured data warehouses 

All security and accountability of sensitive data processing is based on identifying users with certainty (see <u>Annex 7: Identity and authorisation). The data applicants and health data users</u> should be identified in the beginning of the application process and that information needs to be maintained unbroken throughout. This means the official, human-readable document that is the data permit needs to be converted to a machine-readable access permit. This access permit combines the identifiers of the data permit to users' identities and to the newly created dataset that users will have access to. 

An access permit cannot exist before the dataset promised in the data permit has been created and stored with a unique identifier. This new dataset is usually a combination of several source datasets with unnecessary items removed (according to GDPR minimisation principle) and pseudonymised. 

Manual data transfer increases operational complexity and potential risk of human error. Automated streaming based on machine-readable access permits strengthens traceability and compliance with Article 73. The data manager will continue to have full control of the dataset and access to it. They can also make user-requested amendments to data if needed. 

The primary technical requirement to start an SPE federation is to agree on at least one data transfer protocol ( **FSPER-8** ). While EHDS has already committed itself to eDelivery as the secure communication protocol for sending metadata records, data access application forms and messages between national contact point and the EU central platform, the data transfer details have not been agreed on. In practice, there is only one set of implemented community standards that cover the needs of sensitive data transfer and data access management for research: the Global Alliance for Genomics and Health (GA4GH) standards<sup>13</sup> . 

GA4GH crypt4GH<sup>14</sup> is an open source, secure, streaming capable encryption algorithm. It is created for huge genomic sequences but applicable to any file type. The encrypted file is 

> 13 GA4GH implementations https://www.ga4gh.org/our-products/implementations/ 14 Crypt4GH https://www.ga4gh.org/product/genetic-data-encryption-crypt4gh/ 

72 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



separated to header and payload. The payload is encrypted with a key that is stored in the header and never exposed. New user keys can be added and at will. Header can be stored and updated independently of the payload that cannot be decrypted with brute force methods. Sending header and payload separately creates a quantum safe data transfer. Storing crypt4gh headers in a secure database enables automatic user key management for secure data projects. The streaming capability used by GA4GH htsget API<sup>15</sup> can be linked to tokenbased data access control implementing the GA4GH Passport standard<sup>16</sup> . 

These standards are not mandated under the EHDS Regulation but could be considered as candidates for future implementing acts or common specifications under Article 73(5). 

The use of these standards already forms the basis of plans for the framework for the EU One Million Genomes Initiative<sup>17</sup> . Its framework<sup>18</sup> gives detailed information about the initiative that aims to establish itself as a genomics Authorised Participant for EHDS. 

Finally, one of the challenges in manual data management is that many European health data is either not stored in an electronic format at all or not in a standardised format. This makes determining the data applicants' needs and the creation of the needed new dataset difficult. The secondary use of health data should be one more driver towards rapid digitalisation and standardisation of health data at source. 

> 15 GA4GH htsget https://www.ga4gh.org/product/htsget/) 

> 16 GA4GH passport https://www.ga4gh.org/product/ga4gh-passports/ 

> 17 1+MG https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes 

> 18 1+MG framework https://framework.onemilliongenomes.eu/ 

73 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

# **6  Annexes** 

|**Annex number**|**Annex title**|
|---|---|
|1|Methodology|
|2|Public consultation summary|
|3|User journey|
|4|Glossary|
|5|Historical context and legacy models|
|6|Sensitive data life cycles|
|7|Design considerations and expert commentary|
|8|Existing solutions for secure processing|
|9|Overview of relevant EU regulations|
|10|Classification of risks and threats against SPEs|



74 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 1: Methodology** 

The specifications outlined in this report are the result of an in-depth analysis of the EHDS regulatory text, as well as findings from the PwC–Sopra Steria analysis and design of the European Health Data Space infrastructure for secondary use of health data, specific contract under FRAMEWORK CONTRACT N° DI7925-DI7932 European Commission 20222024, existing solutions and project outcomes, and the discussions and feedback received from the Subgroup on SPEs of the Community of Practice. This foundation ensures the specifications are aligned with both regulatory and practical implementation needs. 

A key starting point was the thorough examination of the EHDS Regulation, especially its Article 73 on secure processing environment (SPE) which underpins Task 7.4 and provides essential guidance for the work. This analysis was further enriched by a detailed review of existing SPE solutions and related project outcomes, ensuring a holistic approach to requirements and capabilities. 

Several past and ongoing projects are addressing various aspects of SPEs, providing valuable insights that were analysed to extract relevant requirements and identify reusable approaches. Task partners were requested to suggest relevant projects. The examined projects were primarily selected for their assessment of existing SPEs and their surveys of current infrastructure providers, which eliminated the need for a new survey in this task. Additionally, some projects focus on developing a blueprint for SPEs or are piloting the infrastructure. Including these projects in the evaluation was crucial to ensure alignment among them. These projects are presented in <u>Annex 8: Existing solutions for secure processing.</u> 

The major contributors of Task 7.4 analysed the collected material and conducted in-depth research on various topics according to their specific areas of expertise and interest. The findings were then presented and discussed with all task partners. 

Following the analysis of project results and current requirements for existing SPEs, the next step was to identify gaps and areas for improvement within the current landscape. These results were utilised to establish the minimum functional, operational, security and interoperability requirements for future SPEs. 

A draft version of this document was in public consultation in September 2025. A summary of the stakeholder feedback collected during the public consultation is available in Annex 2: Public consultation summary. 

### **Enterprise Architecture** 

The analysis of SPE environment in this report is presented using The ArchiMate® Enterprise Architecture Modeling Language<sup>19</sup> version 3.2 as implemented by open-source Archi<sup>20</sup> application version 5.6.0. 

> 19 The ArchiMate® Enterprise Architecture Modeling Language <u>https://www.opengroup.org/archimate-forum/archimate-overview</u> 20 Archi https://www.archimatetool.com/ 

75 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



ArchiMate® has not been widely used in biomedical context despite its advantages over other graph generating approaches. ArchiMate® offers a rich selection of conceptual elements that cover from high abstraction level motivation elements through strategy, business, application levels down to technology. The richness of this vocabulary and restricted relations linking elements together form an expressive graphical framework enforcing the separation of abstraction levels. 

Annex 1: Figure 1 presents a simplified metamodel highlighting the business-level elements (in yellow), which represent real-world user-facing functions. These elements are linked to their strategic capacities (orange) and motivational drivers (purple), reflecting how real-world services relate to abstract capabilities and regulatory motivations. 

In architecture terminology, this report focuses on determining the strategic level minimum requirements and describing the capabilities needed for SPEs in different implantation scenarios. 

**Annex 1: Figure 1.** A simplified ArchiMate® metamodel showing the elements used to show how motivational elements (purple) influence strategic elements (orange), as abstract representations of services and their component roles, processes, and objects (yellow). 



<!-- Start of picture text -->
Strategic level Business level<br>Driver Goal © Requirement/7 Capability Business ©)<br>a) ra ay<br>vo K ii<br>Princi id<br>rinciple (0) Competgnces and humanresources H<br>Resource GD Business RoleCD| | | i<br>Processds and models i<br>Resource [D> BusinessFunction (Q) iii<br>nem BusinessProcess cp) -~' |i<br>Data and information systems H<br>Resource OD Business EI j<br>Kb Object<br><!-- End of picture text -->

### **Modality of requirements** 

Requirements are the a priori conditions that capabilities fulfil. The modality of the requirement is given according to the Internet convention IETF BCP 14<sup>21</sup> as summarised in Table 1.1. 

21 S. Bradner, B. Leiba; BCP14; The Internet Engineering Taskforce Best Current Practice; https://www.ietf.org/rfc/bcp/bcp14.html 

76 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Table 1.1.** Words used in capital letters to indicate the modality of the requirement. 

|**Adjective**|**Modal**<br>**verbs**|**Modal verbs**|
|---|---|---|
||**positive**|**negative**|
|REQUIRED|MUST, SHALL|MUST NOT, SHALL<br>NOT|
|RECOMMENDED|SHOULD|SHOULD NOT|
|OPTIONAL|MAY||



77 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 2: Public consultation summary** 

A draft version of this document was in public consultation in September 2025. This document was commented in total for 80 times. The number of responses may contain some duplicates as there was no individual identification and verification required to respond to the surveys. Some respondents have also responded both from data holder’s and data user’s perspective. The responses came from 13 different countries from the EU countries and the European Economic Area countries. Responses from Eastern European countries and international organisations were largely missing. The respondents were primarily from three main types of organisations, listed in order of prevalence: public organisations (41%), academic/research organisations (29%) and private organisations (13%). 

### **Summary of comments** 

The public consultation attracted extensive and constructive feedback from a broad range of stakeholders. Overall, respondents acknowledged the value of the document while also identifying areas where further clarification and development would be beneficial. Stakeholders appreciated the concreteness of the content and recognised that, while further technical specification will ultimately be needed for implementation, the current level of detail is appropriate for a policy guidance document. The document was also commended for clearly identifying key challenges for SPEs and for including annex examples that support knowledge exchange. Terminology was generally considered clear and appropriate. 

Several stakeholders wished for more detailed technical requirements to directly support practical implementation and noted that additional specifications would be required. Concerns were also expressed regarding the clarity of compliance and audit expectations. 

Respondents further observed that operational guidance is limited, particularly with respect to reference architectures, deployment scenarios, and concrete lessons learned. Some EHDS-related requirements were viewed as infeasible or overly costly (especially the exhaustive logging), with concerns also raised about potential privacy implications. Although these issues were addressed in the annexes, stakeholders recommended that they should be explicitly acknowledged in the main text. 

The feedback also pointed to challenges in readability and structure. Requirements were perceived as scattered, repetitive, and at times mixed with recommendations, with insufficient distinction between mandatory and optional elements and unclear allocation of responsibilities. Some terminology was considered misleading, and concepts related to federation were felt to be insufficiently integrated. 

Several comments addressed topics beyond the intended scope of the document, including multi-dataset linkage workflows, privacy-enhancing technologies, synthetic data generation, multi-authority coordination, and payment models. These topics are addressed in other TEHDAS2 deliverables. 

78 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **Report revisions** 

Based on the feedback received through public consultation, the document has been substantially revised and strengthened in several key areas. The revisions focused both on improving clarity and structure, and on ensuring that stakeholder comments were meaningfully incorporated into the final specifications. These have not changed the main outcomes of the report. 

The introduction has been expanded and refined to better express the aims of the report and its scope. Additional context has been provided to explain how the document should be used and how it relates to other deliverables. 

The progression and interdependence of requirements have been clarified. Fundamental drivers are now clearly discussed in relation to GDPR, and the generic SPE section does not refer to aspects related to the EHDS Regulation.  A new explanation has been added describing the logical progression of requirements and how they are interconnected. Requirements for export control and reporting of clinically significant findings that are unique to EHDS SPE are now mentioned in the main report. 

All requirements are presented in tables that follow the same overall structure.  All requirements deriving from EHDS Regulation now have explicit role allocation, directly addressing requests to clarify responsibility for each requirement. 

In response to specific comments, several clarifications have been introduced across the document, focusing mainly on improving the interpretation of requirements and refining terminology. 

The comments received during the public consultation on operational requirements primarily highlighted areas where additional clarification was needed, ranging from the general description of roles to the specifics of individual requirements. As a result, the operational requirements were refined primarily to provide added clarity, ensure proportionality and feasibility, and explicitly address the regulatory, legal, and security considerations highlighted by the consultation. 

Adjustments included reinforcing connections to the data permit, clarifying credential and access management, specifying the minimum scope of auditable and compliance-relevant events, and strengthening the rationale for security, risk management, and software integrity practices. These revisions aim to ensure that the operational requirements offer clear guidance while remaining practical, proportionate, and aligned with EHDS objectives and best practices in information security. 

Several adjustments have been made to the federated computing requirements (FCR). Requirements relating to federated computing are now clearly indicated to be nonmandatory, reflecting the feedback received. While several comments recommended providing more detailed definitions for the implementation of federated learning, it was determined that this level of detail falls outside the scope of the current deliverable. Additionally, feedback regarding the definitions of key terms has been addressed; the definitions of federated computing, federated analysis, and federated learning have been clarified, and the rationale for these concepts from the EHDS perspective has been strengthened. 

79 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

Furthermore, various changes have been applied to the technical interoperability requirements (TIR). These requirements now reference industry standards and make clear that specific technologies mentioned are intended solely as examples. Importantly, the technical interoperability requirements have been revised so that they are applicable to all SPEs, rather than being limited to those involved in SPE federation. 

Several changes have been made to improve the overall structure and coherence of the report. The technical interoperability requirements (TI) have been repositioned to follow the EHDS SPE operational requirements, while the federated computing (FC) requirements are now presented as a subsection of the SPE federation chapter (FSPE) to better reflect their close relationship and avoid fragmentation of related content. 

80 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 3: User journey** 

When a data user applies for electronic health data for secondary use purposes, such as research and innovation activities, education, and policy-making, within the European Health Data Space (EHDS), the user journey consists of several stages (see Annex 3: Figure 1). Access for certain purposes (public or occupational health, policy-making and regulatory activities, and statistics) is reserved for public sector bodies and Union institutions (see Chapter IV, Art. 53(1) and 53(2)). 

**Annex 3: Figure 1.** EHDS user journey consists of five main phases: data discovery, data access, data preparation, use of data and finalisation. 



<!-- Start of picture text -->
Pm onereaon Finalisation<br>QQ ntuene pata, nana (Ucect data Q Data mer<br>Nationa Health date /<br>Ox manatee Q rare somes / tein<br>ad he E--<br>So =... X=<br><!-- End of picture text -->

### **Data discovery** 

Before being able to use the data, the user needs to investigate whether the data needed is available, and whether it is available in the necessary format for the secondary use purpose. This phase is called data discovery. Datasets available in the EU can be found in a metadata catalogue at https://qa.data.health.europa.eu/. Once the data discovery is completed, the user can begin the process of applying for the data. 

### **Data access** 

In the data access phase, the user fills in and submits a dedicated and standardised data access application form or a data request to a health data access body (HDAB). The user must complete the information required in the form, upload necessary documents, and provide justifications as needed. 

81 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Data access application form** is used when the user seeks to use personal level data. **Data request** is for cases when the user wants to apply for anonymised statistical data. 

### **Data preparation** 

During this phase, the data holder(s) deliver(s) the necessary data to the HDAB, which starts to prepare the data for secondary use. Techniques for pseudonymisation, anonymisation, generalisation, suppression, and randomisation of personal data are employed. The data minimisation principle (as per the GDPR) must be respected to ensure privacy. 

### **Use of data** 

In this phase, the user performs analyses based on the received data for the purpose defined in the application phase. Analysing personal level data must be performed in a secure processing environment. The duration of this phase is specified in the Regulation (Art 68(12)). 

### **Finalisation** 

This last phase of the user journey concerns data user’s duties regarding analysis outcomes derived from secondary use of data. Data user must publish the results of secondary use of health data within 18 months of the completion of the data processing in a secure processing environment or of receiving the requested health data. The results should be provided in an anonymous format. The data user must inform the health data access body of the results. In addition, the data user must mention in the output that the results have been obtained by using data in the framework of the EHDS. 

82 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

# **Annex 4: Glossary** 

**Table 4.1.** Key terminology 

|**Term**|**Description**|
|---|---|
|Access permit|Machine-actionable data structure that<br>contains the information from data permit<br>in a standardised format that can be<br>securely transferred and acted on by<br>computer services|
|Anonymisation|The process by which personal data is<br>altered in such a way that a data subject<br>can no longer be identified directly or<br>indirectly. (Directive (EU) 2019/1024 of the<br>European Parliament and of the Council of<br>20 June 2019 on open data and the re-use<br>of public sector information, Recital 52;<br>EHDS Regulation, Recital 92)|
|Authorised user|An authorised natural person or legal<br>person listed in the data permit, giving<br>them the rights to process sensitive data<br>inside a secure processing environment.|
|API|Application Programming Interface|
|Data permit|An administrative decision issued to a<br>health<br>data<br>user<br>by<br>a health data access body<br>to<br>process<br>certain electronic health data specified in<br>the data permit for specific secondary use<br>purposes based on conditions laid down in<br>Chapter IV of EHDS Regulation. (EHDS<br>Regulation, Article 2(2) point (v))|
|Data holder application (a software linked to<br>a secure processing environment)|A software application that provides the<br>data holder with secure digital access to<br>the<br>Secure<br>Processing<br>Environment<br>(SPE). Its core functions include facilitating<br>the upload and download of data in<br>accordance<br>with<br>the<br>data<br>holder’s<br>responsibilities<br>under<br>the<br>EHDS<br>Regulation.|
|Data processor|<br>The data processor should handle data<br>exclusively in the manner prescribed by<br>the controller. A data processor acts under<br>the detailed instructions of the data<br>controller only, by processing personal<br>data on his behalf. (GDPR, Article 4(1)(8))|



83 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**Term**|**Description**|
|---|---|
|Data user application (a software linked to a<br>secure processing environment)|A software application that provides the<br>data user with secure, computerised<br>access to their workspace within the SPE.<br>Its primary functions include facilitating the<br>upload and download of data while<br>ensuring<br>robust<br>authentication<br>and<br>authorisation mechanisms to prevent<br>unauthorised access.|
|EDIC|European<br>Digital<br>Infrastructure<br>Consortium|
|EHD|Personal or non-personal electronic health<br>data (EHDS Article 2(2) point (c)).|
|EID|European Interoperability Framework|
|ERIC|European<br>Research<br>Infrastructure<br>Consortium|
|Federated analysis|A decentralised approach to data analysis<br>where statistical results are computed<br>locally on distributed data resources rather<br>than aggregating raw data centrally. This<br>method enables benchmarking, multi-site<br>research, and collaborative analytics while<br>preserving data privacy and security. Only<br>aggregated insights or summary statistics<br>are shared between nodes, ensuring<br>compliance<br>with<br>data<br>protection<br>regulations.|
|Federated learning|A<br>decentralised<br>machine<br>learning<br>approach where models are trained and<br>validated on distributed data resources<br>without transferring raw data. Instead, only<br>model updates or gradients are exchanged<br>between nodes, enhancing data privacy<br>and<br>security.<br>This<br>method<br>enables<br>collaborative model development across<br>multiple organisations or devices while<br>maintaining local data sovereignty and<br>regulatory compliance.|
|Federated processing|A decentralised data processing approach<br>where computations occur locally on<br>distributed<br>nodes<br>rather<br>than being<br>centralised. This method enables data to<br>remain on local devices or servers while|



84 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**Term**|**Description**|
|---|---|
||only aggregated results or model updates<br>are<br>shared,<br>enhancing<br>privacy<br>and<br>security. It is commonly used in machine<br>learning (“federated learning”), analytics<br>(“federated analysis”), and secure data<br>collaborations<br>across<br>multiple<br>organisations.|
|Federation SPE|Secure processing environment (SPE) that<br>is engaged in federated computing.|
|FTPS|Secure File Transfer Protocol|
|gRPC|Google Remote Procedure Call|
|Health data access body (HDAB)|Member<br>state-designated<br>authority<br>that facilitates the<br>secondary<br>use<br>of<br>electronic health data. HDABs assess the<br>information provided by the health data<br>applicant and decide on health data<br>requests<br>and<br>access<br>applications,<br>authorise and issue data permits, obtain<br>data from data holders and make data<br>available<br>in secure processing environments.<br>HDABs systematically track the data<br>request and data access applications<br>received and the data permits issued.<br>(EHDS Article 55 and Recital 52)|
|Health data user|A natural or legal person, including Union<br>institutions, bodies, offices or agencies,<br>which has been granted lawful access to<br>electronic health data for secondary<br>use pursuant to a data permit, a health<br>data<br>request approval or<br>an<br>access<br>approval by an authorised participant<br>in HealthData@EU. (EHDS Regulation,<br>Article 2(2) point (u))|
|High Performance Computing (HPC)|The use of advanced and not commonly<br>available<br>computational<br>infrastructure – such as supercomputers<br>or<br>compute<br>clusters – to<br>solve highly<br>complex and<br>resource<br>intensive<br>computational problems.|
|HTTP/2|Hypertext Transfer Protocol Version 2|



85 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**Term**|**Description**|
|---|---|
|HTTPS|Hypertext Transfer Protocol Secure|
|JSON|JavaScript Object Notation|
|JWT|JSON Web Token|
|OAuth|Open Authorisation|
|Observational<br>Medical<br>Outcomes<br>Partnership (OMOP) common data model<br>(CDM)|A standardised, common data model<br>(CDM) specification originally developed<br>by the Observational Medical Outcomes<br>Partnership<br>(OMOP)<br>and<br>now maintained by<br>the<br>Observational<br>Health Data Sciences and Informatics<br>(OHDSI)<br>community.<br>It<br>defines<br>a<br>consistent<br>structure<br>and<br>a<br>set<br>of<br>standardised<br>vocabularies<br>for<br>observational<br>health<br>data,<br>enabling<br>researchers<br>to<br>perform<br>large-scale,<br>reproducible analyses across diverse<br>databases.|
|Pseudonymisation|The processing of personal data in such a<br>way that the data can no longer be<br>attributed to a specific data subject without<br>the use of additional information, provided<br>that such additional information is kept<br>separately and is subject to technical and<br>organisational measures to ensure non-<br>attribution to an identified or identifiable<br>person. (GDPR Article 4(5))|
|RDP|Remote Desktop Protocol|
|Representational State Transfer Application<br>Programming Interface (RESTful API)|An application programming interface<br>used<br>for<br>building<br>scalable<br>and<br>interoperable web services. RESTful API<br>follows the principles of Representational<br>State Transfer (REST), using standard<br>HTTP methods to perform operations on<br>resources identified by<br>URLs.<br>It<br>emphasises<br>stateless<br>interactions,<br>meaning<br>each<br>request contains all<br>necessary information without relying on<br>server-side sessions.|
|Secure Processing Environment (SPE)|An environment in which access to<br>electronic health data can be provided in<br>following<br>a<br>data<br>permit.<br>A<br>secure|



86 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



|**Term**|**Description**|
|---|---|
||processing environment is subject to<br>technical and organisational measures<br>and<br>security<br>and<br>interoperability<br>requirements. Specifically allowing access<br>to only those persons listed in the permit,<br>as<br>well<br>as<br>user<br>authentication,<br>authorisation, restricted data handling,<br>logging and the compliance monitoring of<br>respective security measures. (EHDS<br>Regulation, Article 73)<br>Used to mean the SPE service run be the<br>operator<br>and<br>to refer<br>to<br>collective<br>functionalities of SPE user accessible<br>instances.|
|sFTP|Secure File Transfer Protocol|
|SLA|Service Level Agreement|
|SPE project-based user space|Project-based environment within an SPE<br>service that users access. Any shorter<br>versions of this should include either ‘user’<br>or ‘project’ to be clear what environment is<br>meant.|
|SSH|Secure Shell|
|SQLi|SQL Injection|
|TLS|Transport Layer Security|
|TOMs|Technical and Operational Measures|
|Trusted Research Environment (TRE)|A research environment that aims to create<br>trusted, auditable access to sensitive data,<br>often<br>under<br>national<br>governance<br>frameworks. TREs are not the same as<br>secure processing environments, which<br>are<br>legally<br>defined<br>in<br>the<br>EHDS<br>Regulation. TREs emerged from the UK<br>health<br>research<br>sector,<br>shaped<br>by<br>community-led principles and structured<br>around flexible, function-based zones.|
|UDAS|<br>User and Data Access Services|
|URL|Uniform Resource Locator|
|Virtual environment|Virtual<br>environment<br>is<br>a<br>networked<br>application that gives users of simulated<br>experience of something that doesn't<br>directly<br>correspond<br>to<br>underlying<br>hardware.|



87 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

|**Term**|**Description**|
|---|---|
||Commonly used for scalability reasons to<br>maintain<br>simpler<br>environments<br>using<br>vastly more complex hardware.|
|VNC|Virtual Network Computing|
|VPN|Virtual Private Network|
|XSS|Cross-Site Scripting|



88 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 5: Historical context and legacy models** 

The introduction of GDPR at the European Union a decade ago created the need protect sensitive data in way touched all citizens. We are still reeling from the effort to interpret and adapt to it. Sensitive does not mean secret and information is no longer contained in physical documents. The first technical solutions designed for analysing small, structured datasets like statistical information are no longer sufficient. Opening up sensitive data to distributed use brings to the fore the human aspects of these activities that are difficult to contain. 

### **Legacy approach: Secret** 

The topic of securing sensitive data immediately evokes popular images of clandestine operations or military secrets handled behind closed doors. If that sounds familiar, you already have got the wrong end of the stick. Confidential information is where a huge amount of effort is put to keep information as tightly limited as possible to as few people as possible. In contrast, health data for secondary use is meant to be utilised as efficiently as possible for the benefit of the society at large and specifically for future health care choices. The ideas contained and the implications of findings and decisions are meant to be discussed, debated, and published as widely as possible. 

Unfortunately, the technology and therefore vocabulary that we use obscures the distinction between the two. It must be remembered that research on health data has always been done, and it is being done at many different approaches, situations, and purposes. A well-intended regulation that is guided by oversimplification can lead to serious loss of institutional knowledge. 

### **Legacy approach: Physical isolation** 

Confidential legacy is also strongly linked to paper-based approach in information handling. The powerful imagery of red "TOP SECRET" stamped to the corner of the paper permeates popular imagination. Most European national legislations only started changing from databased definition of official information in the 1990s and the effects of that are still seen in practice. The idea of a physical entity holding specific information sits fast. 

In the brave new world of electronic data storage and communication, the realities are quite different. Information can be searched and accessed much faster, flexibly and scalably. Secure storage requirements are conceptually different and need abilities to back up and recover. Sharing, collaboration, and tracking of changes can be automated. Data security becomes paramount to preserve data integrity, prevent unauthorised access, allow auditing and tracking. 

These are the very challenges that carefully designed SPEs and supporting services face when they strive to combine security for improved efficiency, productivity, and collaboration. 

89 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **Legacy approach: Statistical analysis of registries** 

The first implementations of electronic environments tended to focus on statistical analysis of large amounts of social and demographic information from national registries. These analyses have been typically done using standard statistical packages like SAS along with R. The source data are mostly ordered columns of textual and numeric values that require modifications to conform to the needs of the analysis appropriate for the question. 

In other kinds of research, data types can be more varied, datasets significantly larger, the duration of the study much longer, and types of analysis more complex with a need for the development of completely new algorithms and software implementations. For these, the single closed environment created for the purpose of one analysis is a poor fit. A long-term clinical study or genomic study of a rare disease does challenge the boundaries of this approach. They need a more dynamic and distributed environment. That is the current problem of defining how to allow for a controlled and secure ecosystem that combines secure and precise communication to sensitive data services. We will have to draw from the research and practices of large-scale federated data management and combine these to the special needs of secondary use of health data in the context of EHDS. 

### **Technical solutions can never be completely secure on their own** 

Development of sensitive data processing computer environments is driven by increasing security requirements. Although proper risk assessment is supposed to balance the impact of a threat with its probability, there is a clear pressure to keep increasing limiting security features to services. Adding them have the tendency to increase the cost-of-service maintenance and reduce the user experience. The usefulness of new security measures must be considered against the least secure existing aspects of the service. 

In SPE, the graphical interface of the computer that allows the authorised health user to see unprotected health data is that element of least security. It is also the most important for users. Any technical security measures that users do not see the benefit of or make the routine use of the service harder for the user discourages them to use the service at all or prompts them to invent new ways to circumvent these obstacles. 

This implies correctly that non-interactive means of accessing sensitive data can be more secure than interactive ones. This builds a case for query-based sensitive data services where queries and replies can be unequivocally recorded. 

Together, these mean that regulation of authorised users will have to build largely on trust and accountability, i.e. logs. Trust is based on the health data users' willingness and ability in their professional capacity to follow the data access permit. Clear separation of internal and external threat issues and their countermeasures should solve many governance and scalability issues these services face. 

### **Interoperability between SPEs will have a major unifying impact on services** 

The only way secure sensitive data interoperability can be ensured is through shared user and project identity. Only with these, can usage and the flow of information be tracked across a network of services. 

90 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

The establishment of secure and trusted networks of communication between services will make evident the benefits of sharing resources. Many of the resources that SPEs need are available from the Internet but such resources need additional assurances to clear them for sensitive data and a secure communication layer. These in place, these resources will start serving a larger community of services. A prime example is software libraries for commonly used programming languages. 

91 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 6: Sensitive data life cycles** 

The security of data processing inside SPE is tightly dependent on data transfer and supporting services. **Sensitive data access management and interoperability requirements** link SPEs to wider sensitive data cycles (Annex 6: Figure 1) that are common to all sensitive data types and uses, including sensitive intellectual property and consentbased data processing. 

This means that the whole ecosystem where SPEs function must be designed to support modularity and flexibility in order to accommodate different governance models and data flows (Principle 1.3.1. Flexible). 

Both sensitive data management and interoperability depend on reliable and universally applicable **identity management** , which must extend to all participants and services in an interconnected environment. All these services also rely on stable and secure **network connectivity** to ensure availability and communication. 

The generic, high-level use of SPEs (Annex 6: Figure 1) has three use cases for sensitive data processing: 

1. Primary use 

2. Secondary use 

3. Preparation of transient datasets for secondary use 

The primary use might use SPEs for protecting the processing, even in the absence of regulatory obligation. SPE use for safeguarding sensitive data for general use is a major driver for SPE design. SPE should be a convenient way to fulfil the general GDPR and national legislation requirements of due diligence when wanting to protect any kind of sensitive data. 

In the secondary use of sensitive data, the datasets must have descriptive and governance metadata that make them findable and enable the decision-making process of granting access to an identifiable dataset using a data permit. 

When the permitted data is not handed over to the user exactly as it is in the data repository, like when data is first pseudonymised, combined or minimised, the dataset preparation adds another processing step (Transient sensitive data management) before it is ready for the user (TEHDAS2 D7.2 Draft guideline on data minimisation, pseudonymisation, anonymisation and synthetic data). 

92 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 6: Figure 1.** Key capabilities of sensitive data life cycles. 



<!-- Start of picture text -->
Sensitive data life cycles é<br>Tneroperabity Sensitive data<br>i es collection<br>t Sensitive data Senstve nl<br>Mt reception © -<——__________ sseminatonknowledge<br>, x<br>rmaradatas data rai eotina<br>denies ‘| Senate dary Senanvedata<br>esStorage& p--------= === nnn idata n-ne enn nnnenn ena ---m processing Primaryuse<br>metadata<br>+ dat a ,<br>4<br>f<br>H mmebaata Transient Secure Processing al<br>' \ "a Environment (SPE)<br>Sensitive data Sensitive data management,"Sensitive data<br>Brotection << }——| managementasus<br><!-- End of picture text -->

To be maintainable and economically feasible, the specific requirements in EHDS for the secondary use of health data need to fit into these wider SPE ecosystem requirements. 

Annex 6: Figure 2 presents these sensitive data life cycles in a more commonly used linear use case format for easier reading. Capabilities are here directly linked to actors with role names and the functions they perform in EHDS context. 

**Annex 6: Figure 2.** EHDS sensitive data life cycles in linear format with actors. 



<!-- Start of picture text -->
ootegg Ee Secure Processing ff<br>| TR rs<br>———a ecee aTee eTee ie SaasaeIr)<br>as — sy — Pocono<br>cuss ese a. 7 so. aerTransient aaaLi a (ee4<br>ee rene coonnan man ma mh |<br>’ Lae sia ae:<br>ar von | natin Fl a q| eataae 9 | [ae<br>aa 8 me Fl a oa 8<br>ae pag roy<br><!-- End of picture text -->

93 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 7: Design considerations and expert commentary** 

Functional requirements of the SPE cannot be fully separated from the sensitive data life cycles ecosystem (Annex 7: Figure 1). Some of its functional requirements must be shared with the whole ecosystem. This becomes clearer when we consider the needs of data transfer and interoperability that arise from the needs of distributed and federated computing. 

In architecture, a stand-alone SPE concept is abstracted to a capacity that has resources (Annex 7: Figure 1). We will follow the order of active resources to discuss the various aspects of SPE functionalities. 

**Annex 7: Figure 1.** Resource map of SPE capability. 



<!-- Start of picture text -->
Secure Processing Environment (SPE) c<br>Competences and human resources<br>Authoriseduser GD controllerDaa =@ maintainerService @ Reviewer (D><br>Processes and models<br>environmentProject environmentProject (| managementSPE access @<f- ‘Anonymousaccess for (| Data upload (@)<br>creation decommissioning reviewers<br>Permitted data i ‘SPE environment (i> Project Gp User tool Gi) Data backup (i><br>feasibilty evaluation, feasibilty evaluation, hibernation import (duration of<br>reporting, amending Feporting, amending the project)<br>Project member (i) Export from Gi} Log taking @)> Log analysis > Incident D><br>collaborationtools SPE management<br>anonymousExport of @ Returnof (i> Creation of (i> Daa =@ Remote (><br>results/code informationenriching new datasets analysis =<} callserv i ngce<br>Data and information systems<br>Sensitive GD) | User-provided GD ‘Analysis (GD) | Non-sensitive @) | Data permit GD)<br>data sensitive data codetools and auxillary data<br>Clinically @D log data @)<br>significant<br>findings<br><!-- End of picture text -->

### **Identity and authorisation** 

The absolute first requirement of any secure system is that all its users are uniquely and reliably identified (see **SDR-1** ) as stated in the EHDS Article 16. That requirement includes that the chain of trust created by this identification is carried uninterrupted throughout the data application and use. 

EHDS needs national and cross-border authorisation of users on a scale not yet realised within the EU. Therefore, its success will depend heavily on the widespread adoption of European electronic identification system with its cross-border eIDAS network connecting national electronic IDs and their efficient use in the European Digital Identity (EUDI) Wallet. 

94 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

The use of eID for sensitive data processing should require high level of assurance that is equivalent to initial registration of turning up in person and authenticating with an official document<sup>22</sup> . 

Implementing acts and secure protocols underlying the EU Wallets are still under development, raising a possibility that EHDS services will initially need to allow the use of alternative authentication methods that should not be lower than the aforementioned assurance level. Also, the aim of the EUDI Wallet system is to provide identity services first for official uses and the needs of education and research are only fourth in priority list. 

In addition to authorisation, EHDS needs to enable authentication of access to sensitive data with equally high level of assurance. This would allow converting the official, human-readable data permit to machine-actionable access permit that can be used to channel permitted health data to the health data user’s project space inside SPE. 

In Europe, automated research data access authentication services are offered only by Life Science Login (LS LOGIN) by EOSC and ELIXIR that implement GA4GH passports and visas<sup>23</sup> that are secure protocols able to give remote access to electronic resources. 

GA4GH visas allow for additional attributes to be added to the person and the permit (as required in EHDS article 68(1)(d) about needed professional qualifications). Users' ability to access the data could be linked to their affiliation (organisation, position) as well as their abilities to handle sensitive data (see the next chapter Priority of user training). The LS Login currently has "de facto researcher" attribute that ensures that the person has the research status in their current organisation that is not available to EUDI Wallet. The word is out that data spaces will be responsible for implementing the attributes and services they will need to as Wallet verifiable credentials. 

It should be a high priority for EHDS to implement these approaches. Luckily, EU Digital Wallet and GA4GH passport protocols are both based on OAuth and OpenID Connect specifications, making the work easier. 

### **Priority of user training** 

There are three main principles governing the implementation of SPE: 

1. Enabling (Principle 1.) 

2. Privacy (Principle 2.2.) 

3. Accountability (Principle 2.3.1) 

Various technical and operational ways ensure the privacy of data and the accountability of its processing. The enabling SPE requirement **SPER-7** separates the sensitive data from classified information and creates the weakest link in the SPE usage: Users in all practical cases are required to see, learn from its details, and reorganise the sensitive data before it can be effectively analysed. 

> 22 eIDAS <u>https://ec.europa.eu/digital-buildingblocks/sites/display/DIGITAL/eIDAS+Levels+of+Assurance</u> 

> 23 GA4GH passports https://www.ga4gh.org/product/ga4gh-passports/ 

95 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



This has two major consequences. Firstly, users need to understand the responsibility of accessing sensitive data and conversely that understanding needs to be demonstrated to representatives of data controllers before they are given access to the data. Secondly, all security measures directed to data users need to take this weakest link into account. Overdoing measures against authorised users are waste of effort and money, as well as increase the security risk due to user irritation and frustration. 

In other words, if data processing is based on users learning new insights, the system must have trust to the users. This needs to be earned by demonstrating ability to shoulder the responsibility based on clearly defined curriculum. The modular SPE certification framework could be formalised to have several modules covering different levels of necessary knowledge, e.g. sensitive data protection, user responsibilities and penalties under EHDS, specifics of the SPE user. The licence could answer part of the requirements from EHDS Article 68(1) points (d) and (e) for health data applicant to demonstrate their qualifications to perform the intended research (see also previous chapter Identity and authorisation). 

### **SPE as collaboration area** 

The other aspect of the enabling principle is that SPE needs to promote communication between project members to do the data analysis ( **SPER-5** ). The requirements of sensitive data demand that all that communication should happen within the SPE. A prudent principal investigator would immediately set up a shared file that project members will be using as the project logbook. That would allow project members to know exactly what is happening in the project without the risk of revealing sensitive project data to outsiders. 

We need to take that approach even further: SPE should be designed to enable information transfer and communication among project members. While each researcher needs their own private space within the SPE, the default should be that actions and files need to be fully shared. Ideally, all record keeping tools should allow for concurrent editing. This thinking should be extended to ongoing analysis runs so that project members working in different physical locations and time zones stay up to date with the project. The SPE should offer these tools. Similarly, the immediate communication in the form of chats, and phone and video calls should happen within the SPE when the technical capabilities make that possible, like in generic virtual desktops. 

From this point of view, the SPE is a new kind of social experiment in computing. The isolation of the SPE recreates the open and protected environment of isolated mainframes of the late 1960s, when file and user project space protection was in infancy, but enthusiastic users explored the potentials new technology in. This era also saw an explosion of new ideas getting implemented and information was freely exchanged. The roots of the open-source movement are in those times. 

We are still so early in developing the SPE concept that these ideas have not yet turned into guidelines or implementations<sup>24</sup> . 

Finally, the project logbook is a good example of the privacy problems of sensitive data processing. It allows project members to focus on data analysis and use freely identifying 

> 24 Lehväslaiho, H. 2025-06-09 Secure Processing Environment in search of a metaphor. <u>https://research.csc.fi/2025/06/09/secure-processing-environment/</u> 

96 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



pseudonyms in their data. The accountability of their work depends on the accuracy of their log keeping. This raises open questions about how accountability and anonymisation obligations intersect. Further guidance will be needed on retention of project-level collaborative metadata. 

### **Data analysis** 

Data processing involves the software and frameworks provided within the SPE that enable data users to manipulate, transform and extract actionable insights from data. These tools enable the SPE to fulfil its core function, ensuring compliance to secure sensitive data processing rules and protecting against threats. 

By default, in an isolated multipurpose SPE that is based on the secure virtual desktop concept, the data analysis itself should not be that different from normal desktop computing -- apart from lack of direct and open network access. 

SPE environments that are built for specific analysis using pre-installed software for specific purposes, based for example on Jupyter Notebook, can be more straightforward to manage and run. 

Tilting the balance towards more advanced technologies is the reality that building SPEs and their supporting services is an expensive and time-consuming effort. The cost is so high that it would be unrealistic to build a low technology solution for EHDS and develop and maintain simultaneously a higher-end SPE for other purposes. Low-end solutions are quick to set up but have higher running costs with more error-prone human steps. Deploying low-end SPE solutions may lead to higher long-term costs and reduced scalability, making upgrade paths a critical consideration for EHDS infrastructure planning. 

This is where we move the focus of this treatise from abstract to more concrete. Different use cases and implementation choices will strongly affect the flexibility, scalability and capabilities of SPE-based sensitive data processing. 

### **SPE environment management** 

The definition of an SPE regardless of the use case is based on isolation and accountability. The isolation extends to the separation of roles to manage the SPE environment separately from data access and other services maintained within the same organisation. Additionally, it requires that data from different projects are not mixed at any point and a new SPE instance is launched for each of them. 

### **The trusted use case: HDAB** 

The trusted use case (see chapter User stories) of SPE gives the user the freedom to select the environment and modify its details to meet their needs. For the HDAB, this means that the tools that the HDAB data managers need can be largely predicted and pre-installed to the environment where the HDAB data managers bring in the source datasets provided by the health data holders, process them, bring them out of the SPE, and place them for 

97 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



importing or streaming into the distrusted use case SPE for processing according to the data permit. 

### **The distrusted use case: Health data users** 

In the distrusted use case of EHDS, various limitations and restrictions are imposed on the health data user. Under EHDS (Article 61), the HDAB designates the SPE for the health data user based on availability and user needs expressed in the data access application form. The health data user is required to pre-declare their own datasets containing personal data needed in the environment. Depending on the SPE setup, some needed resources (applications, libraries, datasets) will be provided into the SPE environment by the SPE provider (Article 67(2)(i)). In any case, users will need to import various kinds of files into their SPE project space. In an ideal case, there should be no limitations for user imports, but this can depend on the SPE setup (see chapter Cybersecurity of SPE infrastructure). 

The SPE operators might want to agree on minimal security procedures that will allow them to share the burden of preparing them. Annex 7: Figure 2 gives an overview of a proposal under preparation. 

To summarise, security measures should strike a balance between protection and usability. They must not impose unnecessary restrictions or unnecessarily impede researchers’ work. A streamlined process is needed to ensure tools can meet users' needs in a fast and efficient way. 

**Annex 7: Figure 2.** Resource-checking procedure for SPE operators, currently a draft best practice under development by the SPE Community of Practice subgroup (personal communication, Miikka Kallberg, CSC, FI). 



<!-- Start of picture text -->
Unvented > Manual eva<br>Pash pe check<br>><br><!-- End of picture text -->

The first task for users getting access to a new SPE is to evaluate its appropriateness to its intended use. Data controllers, represented by the HDAB, are responsible that the provided data is according to the data permit. The SPE provider should be approached in technical questions about the environment. There should be written instructions for most common problems (as detailed in the chapter Priority of user training). 

98 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



The goals, approaches, and timetables of a project tend to change. Some of these changes will need changes to the data permit. Managing the timely onboarding and offboarding of researchers presents a significant security and operational challenge for projects, which can be addressed effectively with automated identity and affiliation management. It would be convenient if the management of the list of authorised participants could be amended directly by the principal investigator. 

The specifics that are mentioned in the data permit will need to be passed on to the HDAB for recording or approval. The principal investigator of the project carries the main onus that official requirements are fully followed (EHDS recital 62). The requirement of destroying user enriched data from SPE at the end of the project (after 6-month grace period) will cause requests for long extensions to keep the project alive at least until its main findings are published (see further discussion in the chapter Data export from SPE). 

### **Ending and pausing the user SPE** 

At the end of the project, or in case of a detected security incident, the HDAB and the SPE Operator will need to be able to cut access to data or SPE. 

The health data users also need to be able to control the data and processing for security and cost reasons. The project area of SPE always has two main components: storage and analysis. Depending on the SPE implementation, these can be tightly or loosely coupled. A very loose coupling is exemplified by the system where the secure storage is fully independent of the processing component of which there can be multiple instances accessing data (see Operational SPEs in Europe: CSC SD Services) 

Users might need an _SPE backup facility_ to safeguard some intermediate results from their temporary storage area into the secure storage. 

An extended pause in the activities might put a severe strain on the budget of a project. SPE operators should offer an _SPE hibernation_ service to maintain the project in inactive state with significantly lower cost. This same sentiment is expressed in EHDS article 68(12) suggesting that HDAB could store permitted datasets in a system with lower cost to the user. 

### **Monitoring of SPE use** 

Accountability (Principle 2.3.1) is the way to ascertain that the permitted health data user's actions correspond to the rules for sensitive data processing and specifically to their granted data permit. 

Monitoring is the way to implement accountability. User actions are recorded by the SPE operator and monitored for irregularities. However, the legal responsibility of investigating them is on the HDAB. The sharing of executive actions on incidents between the SPE operator and the HDAB needs more clarification, especially when they belong to different organisations. 

The DGA’s definition of an SPE and again the EHDS legislation stress that all user actions must be recorded and be available for auditing. They are usually seen to be the **access log, the transfer log, and the activity log** . The first two record who accesses what service and 

99 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



when, and what is being transferred in or out of the service. They are seen as standard procedures for all services and make perfect sense to monitor those for sensitive data processing SPE. 

The inclusion of obligation to record user activity within the service is highly contentious. It means that each and every action of the user within a service needs to be recorded, regardless if it has to do with sensitive data processing. Very few existing services are known to implement this. We feel this severely violates the user privacy. Their credentials for accessing sensitive data have already been vetted and approved. They have been given access to sensitive data they applied for, making them the data controllers of the approved data limited by conditions in the data permit in an environment that should protect them and sensitive data from outside perusal in addition to promote collaboration among project members. Collecting unspecified personal data on user actions inside the SPE is the kind of activity that GDPR was written to prevent. 

Not only is collecting all user actions a violation of privacy, but it also generates huge amounts of data that is very difficult to analyse. Further, graphical user programmes may do whatever with the data in their memory without leaving any sensible trace in the logs, undermining the usefulness of action logs. The increase in log volume is also significant cost issue. 

The task of logging and monitoring needs to balance scalability with accountability requirements. Continuous monitoring tasks can see the most obvious and often unintentional breaches of requirements. The other end of the spectrum arises from the novelty of research results and the changing sensitivity of information over time as reguired by GDPR. The latter is near impossible and time consuming to define. The cost is that arises either from human labour or automated tools is prohibiting. 

Rather than focusing on action logs of dubious legality and utility, its efforts should be spent on ensuring that exported information is properly identified and anonymised. The chapter 'Data export from SPE' below proposes that all exported data from the SPE should be kept for an extensive period in case suspicions of their appropriateness or accuracy arises later. 

The division of monitoring responsibilities between SPE operator and HDAB should clearly be stated in the implementation act. These cannot be left to be determined separately between each HDAB and SPE nor should they depend and vary on every data permit. SPE provider should do the base monitoring of logs. When an incident is detected, SPE operator should evaluate the severity and pass their significant findings to the HDAB that will take responsibility of the proceedings and ask for more details when needed. 

### **Data export from SPE** 

Data export from the SPE in the trusting use case is role-based without explicit controls required by the regulation. HDAB staff are trusted to keep sensitive data secure outside SPE. They can be trusted to store and distribute the sensitive data responsibly in encrypted format and pass it on to a secure processing environment for further analysis by health data users. 

The untrusted SPE use case under EHDS have three separate cases for data export that have distinct functional requirements for SPE (Annex 7: Figure 3): 

1. Export of anonymous results 

2. Returning of clinically significant results to the original data holders 

100 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### 3. Creation of new datasets of enriched research data 

**Annex 7: Figure 3.** Export from SPE. 



<!-- Start of picture text -->
Sensitive data of Sensitive data a<br>processing ——» _ knowledge<br>dissemination<br>‘SPE B::] Export from Git)<br>+ ‘SPE<br>Distrusting use case 7 i \<br>Export of (i) Return of Gi) Creation of Gi} Archiving of i><br>anonymous enriching new datasets the project<br>results/code information<br>| | | i ‘i<br>Health data CO HDAB Q Health data CO<br>user holder<br><!-- End of picture text -->

### **Export of anonymous results** 

EHDS requires HDABs to verify that exported results are anonymised, but it does not specify the method for performing such verification (Article 73(1)(f)). Member States or HDABs may develop tools or guidelines to support this obligation. The implementing acts under Article 73 may also provide common EU-level requirements or procedures to ensure consistency. Pseudonymisation and non-sensitive data types such as anonymised and synthetic data are covered in TEHDAS2 D7.2 Draft guideline on data minimisation, pseudonymisation, anonymisation and synthetic data. 

Export of anonymous results may be divided to two major steps: (1) generation of anonymous results from analysed data and export of it by the health data user and (2) monitoring of the exported files for anonymity by the HDAB (EHDSR-13). 

The feasibility of these tasks ranges from straightforward (exported information in code or large numbers of register data in aggregated format) to outright impossible (complex mix of data types). 

It should be noted that health data users can be expected to export not only final analysis results for publication, but also intermediary results and the frequency and volume of these ones can be high. 

101 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

Most obvious mistakes in anonymisation can and should be semi-automatically detected before the export is allowed to happen. Tools and guidelines are currently being developed (see e.g. <u>Anonymity verification tool (Finland), Handbook on Statistical Disclosure Control for</u> Outputs<sup>25</sup> , and the PHASE IV AI project deliverable 5.3<sup>26</sup> ). Related efforts include the SACRO-project<sup>27</sup> , which explores semi-automated checking of research outputs to identify potentially sensitive content. 

Ultimately, the requirement of checking all output from open-ended scientific research, even by reviewing, can be extremely difficult. HDABs would need personnel who are experts in all health research domains who would spend long time trying to understand the risks of exports. 

A more scalable approach would be to focus on helping researchers to anonymise their results effectively by training and automated feedback tools and store all output results as if they were logs of activities. Analysis of results anonymity would be a part of the required continuous activity of HDABs that can be subjected to more thorough reviewing in case of a security concern. 

### **Returning of clinically significant results** 

Clinically significant findings (EHDS Article 65(5)) are an exception to the rule that health data users can export only anonymous data from the SPE (Annex 7: Figure 4). While the process is to export out of the SPE, sensitive data is not seen to leave the EHDS secondary use domain as it is to be transferred securely to the HDAB who has the responsibility to inform the original data holders for the ultimate purpose of letting the citizen to know. The details of this process will be decided by member states. 

Still, from the SPE service implementation perspective, this is an export of personal information from the closed environment that differs from other exports only in having a different recipient. 

> 25 Handbook on Statistical Disclosure Control for Outputs https://securedatagroup.org/guides-and- <u>resources/sdc-handbook/</u> 

> 26 The Phase IV AI project D5.3 https://www.phase4ai-project.eu/wp-content/uploads/2025/09/D5.3_- <u>Data-Hub-Design-and-Data-Market-v1_PU.pdf</u> 

> 27 SACRO https://dareuk.org.uk/how-we-work/previous-activities/dare-uk-phase-1-driver- <u>projects/sacro-semi-automated-checking-of-research-outputs/</u> 

102 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 7: Figure 4.** The EHDS outline for the procedure for clinically significant findings from SPE. 



<!-- Start of picture text -->
Informsignificantnatural personsof 57<br>f=)<br>SPE findings<br>Recital67 (J) Significant a<br>° CS<br>CreateEHDS guidelines Board CO]()-» | Authorised| CD Healt¥ Data_CO)£ Informing naturalHealth persons¥  data of significantCo)  findings ¥Heath CO) Ei¥ Natural CDa<br>healthuser data —inform® Access(HOAB) Body holder —» professional ~—» person<br>2 a National law (J) |<br>Article 942) (<br>© Article 615)() Article 58) (J) Right to not 77<br>| | | be informed<br><!-- End of picture text -->

### **Creation of new datasets of enriched research data** 

EHDS does not give any guidance on reusing datasets cleaned and enriched by health data users, and this is generally seen to be outside the basic EHDS use case.  Enrichment is mentioned in the EHDS recitals. 

Two main arguments may be raised in favour of reusing of datasets enriched in research. The effort of cleaning, harmonising and combining of research data for analysis is often the most time-consuming part of the work. From the practical point of view, throwing this away is this massive waste of effort will have to be again for any updated analysis. At a more philosophical level, this goes against the principle of sharing and the results of enriched data for future studies (Principle 1.1.4. Reusable in FAIR). 

The **TEHDAS2 Deliverable D5.4: Short Guide for Data Enrichment for HDABs, Data Holders, and Data Users** will have guidance for returning enriched data to data holders.  In addition, member states are recommended to consider enabling national legislations for storing and reusing of their health datasets. 

Enriched datasets can be seen to cover two distinct situations: 

**Enhanced versions of original datasets** – This refers to datasets whose quality or structure has been improved (e.g. through cleaning, deduplication, harmonisation), without combining personal data from multiple sources. These may, under certain conditions, be returned to the original data holder within the EHDS framework, especially if no new personal data are added or created. 

**Newly created datasets resulting from linkage or analysis** – These are research outputs combining data at the individual level from multiple sources. Distributing would raise significant concerns about data controllership, re-use conditions, and compliance with the 

103 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
bag<br><!-- End of picture text -->

EHDS secondary use rules. These datasets cannot be exported or reused unless they are fully anonymised or covered by a clearly defined legal exception. 

If these ELSI aspects can be solved, the practical solution for restricted access datasets are offered by the European Federated EGA services<sup>28</sup> . Federated EGA requires that researchers depositing datasets are members of research organisations that guarantee their identity and trustworthiness and will act as the broker for re-use requests of datasets. 

### **Scenarios** 

We will somewhat arbitrarily divide available implementation options to three that we call local, state-of-the-art, and distributed (Table 7.1.) that will enable progressively more capabilities and choices for data processing. Most existing SPE environment solutions already combine their features across these simplistic categories. 

**Table17.1.** Implementation options 

|**SPE Capabilites**<br>~~rr~~|**Local**|**State-of-the-art**|**Distributed**|
|---|---|---|---|
|**User identity**<br>|Local|Federated|Federated|
|**Data protection**|Full|Full|Full|
|**Key management**|Manual|Automatic|Automatic|
|**Data access**|Local copy|Managed,<br>streamed|Managed,<br>streamed|
|**Interface**|Virtual<br>machine or fit<br>for<br>purpose<br>restricted<br>access|Virtual machine|Federation<br>services<br>for<br>distributed<br>service<br>provision across<br>organisations|
|**Service type**|SaaS|PaaS||



The local scenario represents a situation where the hosting organisation starts from scratch building an SPE from a virtual desktop by securing its operating system and deploys an automation tool inside a secured local network. Users need to be initially authenticated manually and assigned a local identity that will be enabled to a designated virtual desktop. The desktop image will need to be installed with most or all user tools and data need to be copied to the desktop once service providers and possibly users have installed their software products, and it has been secured. The requirement to keep sensitive data encrypted in storage and during transfers causes complications in encryption key management. 

28 FEGA https://ega-archive.org/about/projects-and-funders/federated-ega/ 

104 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



The local scenario can reach a high level of data security but at higher maintenance cost arising from the cost of manual labour. More people involved always increases the administrative cost of minimising human error. It is likely that a manual solution cannot effectively enough secure the SPE user environment to allow users to manage their own runtime software installations, making them more dependent on the service provider. This classifies the service as Software as a Service (SaaS). 

The state-of-the art SPE system uses more effectively supporting services. User identification to high level of assurance is outsourced to their host organisation or country of origin (See <u>Identity and authorisation). Access control to the SPE and project data is controlled directly</u> by the data controller. The human-readable data permit is converted to a machine-readable access permit that automatically links permitted users and data to the project. Data is stored independently of its use and streamed by demand to the SPE project space. The lack of error-prone human intervention to SPE management and high degree of data protection by design and by default (GDPR Article 25) allow for Platform as a Service (PaaS), where users are able to manage their application environment themselves (See <u>Cybersecurity of SPE infrastructure).</u> 

To future-proof sensitive data processing, we need to carefully think what current sensitive data services can do, what is just becoming reachable based on research activities on public data computation, and what needs to be added to them to make sensitive data processing possible in them. 

The first step is clear: We need to widen our thinking of secure processing environment (SPE) beyond a single predetermined virtual desktop. **The concept needs to include all types of processing of special categories of sensitive data** that follows the defined principles, regardless of place or time: 

### **SPE implements sensitive data processing** 

According to this, the desktop is the place where the user interacts with sensitive data, either directly or indirectly. 

For the EHDS health data user experience, this means that the user is allowed to initiate processing tasks that have been audited to be part of the EHDS federation or explicitly mentioned in the data permit. 

What this means in practice will need a more detailed look into various processing options and modern cryptographic abilities. 

Annex 7: Figure 5 provides one way to classify different processing approaches. The current SPE concept can be detached from physical location by implementing the desktop into ephemeral containers that can be executed in multiple compatible platforms (Serverless compute). 

105 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 7: Figure 5.** Sensitive data processing approaches. 



<!-- Start of picture text -->
Physically HPC a:<br>Isolated systems<br>Sensitive data (2 [EET ET)<br>processing<br>SPE a: Remote query Federated af<br><$+--— computing computing<br>Serverless oH Independent 4<br>compute agents<br><!-- End of picture text -->

Allowing a user to send an interactive query to a remote server (Remote query computing), can dissociate the user from the externally managed sensitive data. This increases the security but may distance the user from immediate experience of data. The main questions to ask from a remote query are 1) the permissibility of the query and 2) are returned answers to query sensitive. 

High Performance Computing (HPC) utilises massively parallel and interconnected computer systems that by design have been built to be shared simultaneously with multiple users. The challenge is to allow for isolated queuing and executing of sensitive data jobs without leaking any personal data. The implementation must ensure that the job submitter has permission to the processed data (see an example of HPC sensitive data processing). 

Queries can be automatically sent to more than one target processor and results returned to the sender or the query itself can be the model to be trained, opening increasingly complex possibilities (see Implementing federated computing) with their own requirements. 

Finally, while the processing in an SPE may be anything from simple command line tool execution to complex black box of a large language model (LLM) implementing artificial intelligence (AI), the demand for ever more complex reasoning is driving the development for independent and interacting agents that look for and evaluate information (Independent agents). 

106 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 8: Existing solutions for secure processing** 

The Annex 8 gives a listing of SPEs in Europe and brief explanations of some past and current projects. They provide a solid groundwork for SPEs in the EHDS, emphasising a balance between security, computational performance, and interoperability. These insights will guide the development of SPE specifications in TEHDAS2 and EHDS, ensuring that health data can be processed securely and efficiently while complying with European legal standards. 

Contents: 

- <u>Operational SPEs in Europe</u> 

   - <u>TEHDAS1</u> 

   - <u>Five Safes</u> 

   - <u>Trusted Research Environments</u> 

   - <u>DARE UK</u> 

   - <u>EOSC-ENTRUST</u> 

   - <u>HealthyCloud</u> 

   - <u>Global Alliance for Genomics and Health (GA4GH)</u> 

   - <u>GDI and 1+MG</u> 

   - <u>Sensitive Data HPC strategy (CSC, Finland)</u> 

- <u>NORTRE, infrastructures for sensitive data in Norway</u> 

   - <u>Secure Data Transfer solution (Finland)</u> 

   - <u>Anonymity verification tool (Finland)</u> 

   - <u>Building a secure health data network (Norway)</u> 

### **Operational SPEs in Europe** 

Assessing existing SPEs provides a basis for developing technical specifications. Examining national implementations helps identify best practices for EU-wide adoption while also uncovering gaps, inconsistencies, and areas for improvement. This ensures that the specifications address emerging challenges and strengthen interoperability between SPEs. 

15 operational SPEs across Europe that process individual-level health data for secondary use have been identified and are listed below (Table 8.1). Environments limited to internal organisational use or specific projects have been excluded. Other relevant SPEs may exist but were not identified within the scope of this analysis. 

**Table 8.1.** Examples of operational SPEs in Europe 

|**Organisation**|**Country**|**Name**|**Access**<br>**type**|**Website**|
|---|---|---|---|---|
|The Danish<br>Health Data<br>Authority|Denmark|The Secure<br>Research<br>Platform|Virtual<br>Desktop|https://sundhedsdatastyrelsen.dk/da/english/hea|
|Social and<br>Health Data<br>Permit|Finland|Kapseli|Virtual<br>desktop|https://findata.fi/en/kapseli/|



107 



<!-- Start of picture text -->
BR<br><!-- End of picture text -->

D7.4 Technical, functional and security specifications of Secure Processing Environments 

|Authority<br>(Findata)<br>|||||
|---|---|---|---|---|
|The<br>wellbeing<br>services<br>county of<br>Southwest<br>Finland<br>(Varha)<br>~~C~~|Finland<br>~~T~~|Atolli<br>|Virtual<br>desktop<br>|https://www.auria.fi/tietopalvelu/en/atolli/index.ht<br>~~=~~|
|HUS Helsinki<br>University<br>Hospital<br><br>~~|~~|Finland<br><br><br>~~|~~|HUS<br>Acamedic<br><br><br>~~|~~|Virtual<br>desktop<br><br>~~-~~|https://www.hus.fi/en/research-and-education/hu<br><br>~~———~~|
|CSC – IT<br>Center for<br>Science<br><br>~~e~~<br>|Finland<br><br><br><br>|SD Desktop<br><br><br> <br>|Virtual<br>desktop<br><br> <br>|https://research.csc.fi/-/sd-desktop<br><br>~~ee~~<br>|
|Esior Ltd.<br><br>|Finland<br><br>|SPESiOR<br> <br>|Virtual<br>Desktop<br> <br>|<sup>https://esior.fi/en/spesior/</sup><br> <br>~~———~~|
|Statistics<br>Finland<br><br>~~E~~|Finland<br><br>~~T~~|Fiona<br><br>|Virtual<br>desktop<br> <br>|https://stat.fi/tup/tutkijapalvelut/fiona-etakayttojar<br> <br>~~——~~|
|Health Data<br>Hub<br>|France<br>|HDH<br>Technological<br>platform<br>|Virtual<br>desktop<br>|https://www.health-data-hub.fr/page/faq-english<br>|
|Central<br>Statistics<br>Office|Ireland|Researcher<br>Online<br>System for<br>Applications<br>(ROSA)|Virtual<br>desktop|https://www.cso.ie/en/media/csoie/aboutus-new/|
|Statistics<br>Netherlands<br>(CBS)|Nether-<br>lands|Remote<br>access<br>environment|Virtual<br>desktop|https://www.cbs.nl/en-gb/our-services/customise|



|<br> <br>bag|D7.4 Technica<br> <br>|l, functional and secur<br> <br>|ity specificatio<br> <br>|ns of Secure Processing Environments<br>108<br>|
|---|---|---|---|---|
|The<br>Statistical<br>Office of the<br>Republic of<br>Slovenia<br>(SURS)<br>|Slovenia<br>|Remote<br>access<br>environment<br>|Virtual<br>desktop<br>|https://www.stat.si/StatWeb/en/StaticPages/Inde<br>|
|NHS Digital<br>|UK<br>|Secure Data<br>Environment<br>(SDE)<br>|Virtual<br>desktop<br>|https://digital.nhs.uk/services/trusted-research-e<br>|
|NTNU –<br>Norwegian<br>University of<br>Science and<br>Technology<br><br>~~p~~|Norway<br><br>|HUNT Cloud<br><br>|Virtual<br>desktop<br><br>|https://about.hdc.ntnu.no/ <br><br>~~p~~|
|University of<br>Oslo (UiO)<br><br>|Norway<br><br>|Services for<br>sensitive data<br>(TSD)<br> <br>|Virtual<br>desktop<br> <br>|https://www.uio.no/english/services/it/research/s<br> <br>|
|University of<br>Bergen (UiB)<br><br>|Norway<br><br>|SAFE<br>(secure<br>access to<br>research data<br>and e-<br>infrastructure)<br><br>|Virtual<br>desktop<br><br>|https://www.uib.no/safe <br><br>|



### **TEHDAS1** 

TEHDAS1 deliverable D7.2<sup>29</sup> provides an in-depth analysis of SPEs as defined in the EHDS legislative proposal, along with guidelines covering technical, information security and interoperability requirements. 

The report indicates that the preferred architectural model for SPEs is a decentralised system where multiple SPE providers across different EU Member States can offer compliant environments. This model also supports a federated learning approach, where data stays within national boundaries, but models and insights can be shared across borders. Each SPE would adhere to common EU-wide standards, ensuring interoperability and trust among 

> 29 D7.2. Options for the services and services architecture and infrastructure for secondary use of data in the EHDS https://tehdas.eu/tehdas1/results/tehdas-proposals-for-the-implementation-of- <u>ehds-technical-infrastructure/</u> 

109 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

Member States. This approach also facilitates cross-border research while maintaining national control over data. 

Additionally, the report emphasises that SPEs are not only security-focused but must also be flexible enough to handle a wide range of computational tasks. This includes everything from basic data analysis to more complex tasks like deep learning and artificial intelligence (AI). Given the increasing reliance on advanced computational techniques in health research, SPEs should be equipped to utilise high-performance computing (HPC), GPUs, and other advanced computing resources. Systems must be scalable to accommodate large datasets and resource-intensive processes, without compromising security. 

To fulfil the requirements of the services outlined in Article 73 of the EHDS Regulation, the key functional capabilities for SPEs identified in TEHDAS1 are as follows: 

- **Data Processing Capabilities** : Advanced analysis tools to handle sensitive data, including statistical software, AI libraries, and version control systems for code management. 

- **Interactive Access:** Secure, remote access options such as remote desktop and secure shell connections. Some SPEs may also offer API-based access to support federated analysis. 

- **Strong Access Control** : Comprehensive access management (data holders for data deposition, data users for data analysis, and system administrators for SPE operations) 

- • **Controlled Communications** : Data imports, exports, and other outbound communications. 

- **High Security Standards** : Adherence to stringent security measures to protect data integrity and confidentiality. 

- **Defined Operational Protocols:** Clear, well-documented procedures governing the operation and management of the system. 

SPEs must also integrate harmonised security measures across the EU, allowing for consistent and reliable processing environments. This approach promotes cross-border data collaboration, with interoperability as a key consideration. To this end, SPEs must support standardised interfaces and protocols for seamless data sharing and access management. This ensures that data can be processed and analysed across different countries while maintaining a high level of security and legal compliance. Aligning security standards with recognised frameworks such as ISO/IEC 27001 and ENISA guidelines is recommended. 

### **Five Safes** 

The concept of Five Safes – a framework for planning confidential data governance and management solutions has emerged and evolved in the United Kingdom over the past two decades. 

The Five Safes framework has been initially conceived to help establish a virtual microdata research data centre at the UK Office for National Statistics in 2003<sup>30</sup> . Since then, it rose to international prominence and has been adopted as governance/data management standard 

30 Green, E., & Ritchie, F. (2023). The Present and Future of the Five Safes Framework. Journal of Privacy and Confidentiality. doi: https://doi.org/10.29012/jpc.831 

110 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



for introducing (or retrofitting) various confidential data access solutions in the UK, the statistical offices in Canada, Australia, New Zealand, Norway, as well as Eurostat. Moreover, the framework has been built into or has influenced legislation such as Digital Economy Act in the UK and several state laws in Australia. 

The Five Safes defines five dimensions of confidential data management: safe projects, safe people, safe settings, safe data and safe outputs. These are often formulated as "key questions" (Table 8.2). 

**Table 8.2.** The Five Safes and key questions (Green & Ritchie, 2023) 

|**Element**|**Typical question**|**Example of problems being addressed**|
|---|---|---|
|Safe<br>projects|Is this appropriate<br>use and<br>management of<br>the data?|- What is the purpose of the access request?<br>- Is this an ethical and lawful use of the data?<br>- What is the benefit to society or to the organisations<br>sharing data?<br>- Is there a data management plan in place?<br>- What happens to the data at the end of the project?|
|Safe people|How much can I<br>trust the users to<br>use the data<br>appropriately?|- Do the users have the necessary technical skills?<br>- Do the users need training inhandling confidential data?<br>- Are users likely to follow procedures?|
|Safe<br>settings|How much<br>protection does<br>the physical<br>environment<br>afford to the<br>data?|- How are data stored?<br>- Are there physical restrictions on the users?<br>- Does the IT prevent unauthorised use?<br>- Are mistakes by authorised users likely to be detected?|
|Safe outputs|How much risk is<br>there in the<br>outputs of the<br>access breaching<br>confidentiality?|- If the aim of access is to produce statistics, is there any<br>residual risk by, for example, showing outliers?<br>- If the aim of the access is to produce data for onward<br>transmission, how do we make sure that the released data<br>are appropriate for the next use?|
|Safe data|Is the level of<br>detail in the data<br>appropriate?|- Is there sufficient detail to allow the project to go ahead?<br>- Is there excessive data not necessary for the project?|



As Green & Ritchie underline, the dimensions are not limits, they are scales. What "safe" means, or how restrictive the safety requirements of each dimension are, is dependent on the context. For example, for open data, only the Safe Data dimension must be controlled. In 

111 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



a secure compute environment, data is safer, perhaps it needs to be deidentified only, while there is a higher degree of control across other dimensions.  This flexibility goes hand in hand with "principle-based" approach to designing governance and legal measures. 

In modern understanding, the Five Safes are an aid in identifying structures and goals of a particular confidentiality solution, not a rigid set of guidelines or rules. The right way to approach a design of a system according to the Five Safes is an analysis of the approach to the design problem, then specification of broad principles and aims of the solution, followed by using the Five Safes to provide the structure and, finally, identifying the good/best practices in each area of Five Safes. 

### **Trusted Research Environments** 

Based on the Five Safes framework, the past two decades have seen the rise and adoption of the Trusted Research Environments (TREs), particularly in the United Kingdom, as a safer computer environment to protect the identity of human genomic sequences and then expanded to cover health and social data. The TREs are now seen as the preferred approach (DARE UK, 2024) to ensure the safety of processing of any sensitive data. While there exists a set of community-defined requirements and a derived high-level architecture, interestingly, TRE does not have an agreed definition. It has been called by many alternative names like Secure Data Environment (SDE by the England National Health Service) or Data Safe Heaven (Scotland), and the TRE specification allows it to be organised in many ways. 

The DARE UK Federated TRE Blueprint<sup>31</sup> clarifies the concept by specifying three functional zones that any TRE may contain in any combination: 

- **Research Analytics Zone (RAZ)** for project-specific data processing by users 

- **Secure Data Zone (SDZ)** for active data management roles of data governance 

- **Query Management Zone (QMZ)** to provide secure remote data access services 

In an extreme case, a TRE can be composed only of RAZ making it impossible to draw any functional conclusions from the name. Any practical discussion about TRE functionalities should now indicate the zone. 

Both Research Analytics Zone of TRE and SPE are based on securing sensitive data privacy within a secure computer environment for the exclusive use by data users. Both isolate users by project and demand clearly defined, limited, and secure interfaces out of them<sup>32</sup> (see Annex 8: Figure 1 and Figure 2). 

> 31 DARE UK Federated TRE Blueprint https://zenodo.org/records/14192786 32 Lehvaslaiho H. (2025) SPE and TRE terminology for sensitive data processing <u>https://zenodo.org/records/15696511</u> 

112 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 8: Figure 1.** Equivalence of SPE and TRE-RAZ. 



<!-- Start of picture text -->
Sensitive data 44] Data user CD)<br>processing -———\—__<br>Trusted Reseach 4<br>Environment (TRE) zg<br>Research a: Secure Processing oH]<br>Analytics Zone Environment (SPE)<br>(RAZ)<br>Secure Data Zone uf<br>(SDZ)<br>Query F::|<br>Management Zone<br>(QMZ)<br><!-- End of picture text -->

**Annex 8: Figure 2.** SPE and TRE-RAZ may contain multiple isolated project environments that have only secure and limited access to the outside. 



<!-- Start of picture text -->
Secure interfaces {i}<br>User access (}<br>Management (i> Service lane) Data user CD<br>access ————__ management<br>| |<br>Data SPE & TRE-RAZ uf] Project (1) Unencrypted<br>transfer ——s <—\e environment —— data<br>1+<br>Monitoring (i> i i<br>Compute {1} Storage (><br>Query i}<br>interfaces<br><!-- End of picture text -->

113 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



### **DARE UK** 

The DARE UK (Data and Analytics Research Environments UK) project is a UK-wide initiative aimed at developing a coordinated, trustworthy, and secure national data research infrastructure. It is designed to support research using sensitive data (like health and administrative data) in a way that is safe, ethical, and for public benefit. In its first phase (2021-2024), it focused on developing the technical and governance foundations. The outputs of the projects<sup>33</sup> were categorised according to four of the Five Safes: 

- Safe data: Semi-automated Risk Assessment of Data Provenance and Clinical Free-text in TREs (SARA) aimed at using machine learning to better understand privacy risks in the free-text data. 

- Safe outputs:  Semi-automated Checking of Research Outputs (SACRO) focused on introducing efficiencies into checking research results for disclosure risk before they leave TRE. 

- Safe projects: Maintaining the safety of projects spanning multiple TREs (TRE-FX and TELEPORT projects). 

- Safe settings: the SATRE project set out to assimilate the essential features of TREs into a common specification and provide a first blueprint for new TRE builders. 

The currently ongoing phase two of the project has yielded a blueprint for a federated TRE architecture<sup>34</sup> . For this work, of particular interest are the SATRE specification and the federated architecture blueprint. 

### **SATRE** 

_SATRE (Standardised Architecture for Trusted Research Environments) started as a DARE UK Driver Project working to standardise access to secure data in trusted research environments, and included University of Dundee, Alan Turing Institute, UCL, Ulster University, and Research Data Scotland. (_ SATRE website<sup>35</sup> _)_ 

A major outcome of the project has been a standard architecture specification for Trusted Research Environments. The specification is pertinent to TEHDAS2 specification as it defined key capabilities of a general TRE and a comprehensive list of criteria that can be used to evaluate compliance against the framework of any given TRE solution. 

The four key capabilities – or pillars in SATRE parlance – are<sup>36</sup> : 

- Information Governance 

- Computing Technology and Information Security 

- Data Management 

> 33 DARE UK (Data and Analytics Research Environments UK). (2024). The 2023 DARE UK Driver Projects: Summaries and lessons learned. Zenodo. https://doi.org/10.5281/zenodo.11443328 34 DARE UK. (2024). DARE UK Federated Architecture Blueprint (2.2). 

> 35 SATRE https://satre.uktre.org/en/page/about/ 

> 36 SATRE Specification. https://satre-specification.readthedocs.io/en/stable/ 

114 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



• Supporting Capabilities 

The _Information Governance_ pillar consists of requirements ensuring information risk is measured and managed to an acceptable level (EHDS Article 73). 

The _Computing Technology and Information Security_ pillar lays out a set of technical requirements related to the systems used to secure, manage and provide compute capabilities to _Data Consumers_ . 

The _Data Management_ pillar is concerned with managing data assets while they exist (temporarily or permanently) within a TRE. Note that some of the requirements, particularly those that concern data management from the point of view of a data holder are beyond the scope of an EHDS compliant SPE. 

The _Supporting Capabilities_ pillar is only indirectly associated with a SPE provider. Most of the requirements are related to HDAB itself. 

### **SATRE Roles and their Relation to the EHDS SPE** 

SATRE Project also defined roles belonging to different stakeholders involved with the data lifecycle<sup>37</sup> . The roles may fit well the _health data permit-based_ project concept as data processing roles are tied to natural persons, as well as the kind of expertise needed to run a SPE provider. 

The role of a _Data Consumer_ aligns with _health data users_ as defined in the EHDS legislation<sup>38</sup> . In particular, _Project Manager_ maps to the role of Principal Investigator under EHDS (Article 68). The role of _Data Analyst_ corresponds to any authorised natural person who accesses the data with the purpose of processing. 

The Data Management roles are broadly applicable to organisations which curate the data in addition to providing it in a SPE. In this sense, they may be beyond the scope of an EHDS SPE directly --- except for _Output Checker_ , who may need to be listed on a health data permit with the responsibility of ensuring that no confidential data exists in the outputs of SPE project, the data which is supposed to be released out of the secure environment. 

The SATRE roles concerned with infrastructure management describe the governance needs of an _SPE Operator_ , in order to be applicable to the broadest community of existing SPE providers. 

> 37 SATRE specification role https://satre-specification.readthedocs.io/en/stable/roles.html#roles 

> 38 Directorate-General for Health and Food Safety. (2025, 03 05). Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. Retrieved from European Commission: https://health.ec.europa.eu/publications/regulation-eu-2025327-european-health-data- <u>space-and-amending-directive-201124eu-and-regulation-eu_en</u> 

115 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
i<br><!-- End of picture text -->

## **EOSC-ENTRUST** 

Launched in March 2024, EOSC-ENTRUST<sup>39</sup> is a three-year initiative that brings together partners from 15 European countries to advance the development and interoperability of TREs. These environments play a critical role in enabling secure and compliant access to sensitive research data. 

At the heart of the project is the development of an Interoperability Blueprint<sup>40</sup> , a foundational framework that outlines how sensitive data can be accessed and analysed across a federated network of composable TREs. By addressing both technical and policy-level interoperability, EOSC-ENTRUST supports the broader goals of the European Open Science Cloud (EOSC) and is working under both the EOSC and ELIXIR umbrellas. The project also maintains strong ties with other ELIXIR and European Commission-funded initiatives and is aligned with the EuroHPC infrastructure to explore high-performance computing for secure data analysis. 

A key objective of EOSC-ENTRUST is the establishment of a Provider Forum, a community platform for SPE/TRE providers to exchange knowledge, share best practices, and collaborate. This forum is designed to continue beyond the project’s lifetime, ensuring sustained support and onboarding of new providers into the ecosystem. 

The project is also developing complementary tools and resources, including: 

- A set of Training Packages for TRE providers and users, 

- A machine-readable TRE Provider Catalogue that maps available secure environments within EOSC, along with their capabilities. 

EOSC-ENTRUST’s work is driven by diverse use cases, or “Drivers,” which include: 

- Federated human genomics, 

- • Social science data sharing, 

- Clinical research data interoperability, 

- • Public-private collaboration involving health and environmental data. 

To maximise relevance and impact, EOSC-ENTRUST closely aligns with related European initiatives. In particular, the project collaborates with TEHDAS2 in support of the EHDS, and with the Genomic Data Infrastructure (GDI) for genomics-related use cases. These connections help ensure that EOSC-ENTRUST complements ongoing efforts and contributes meaningfully to a cohesive European data ecosystem. 

Throughout the project, EOSC-ENTRUST will also follow the project outcomes of its sister projects SIESTA (Secure Interactive Environments for SensiTive data Analytics) and TITAN (Trusted envIronments for confidenTiAl computiNg and secure data sharing), which are 

> 39 EOSC-ENTRUST https://eosc-entrust.eu/ 

> 40 Sætrom, P., Lehväslaiho, H., Stansberg, C., Awan, H., & Hesam, A. (2024). EOSC-ENTRUST D13.4 Year one version of EOSC-ENTRUST Blueprint & Interoperability Framework. <u>https://doi.org/10.5281/zenodo.14362388</u> 

116 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



funded under the same HORIZON 1.3 call on Trusted environments for sensitive data management in EOSC. 

### **HealthyCloud** 

The HealthyCloud project aimed to lay the foundation for a European Health Research and Innovation Cloud (HRIC) by promoting the secure, ethical, and efficient sharing and reuse of health data across Europe. It brought together a wide range of stakeholders to define a strategic agenda and develop a practical framework to support cross-border health research and innovation, while ensuring compliance with legal and ethical standards. 

Within this context, the objective of Deliverable D5.1 (confidential and unpublished) was to identify common patterns in the design and operation of SPEs, focusing on key requirements that could inform the development of reference guidelines for the planned HRIC. The report draws on in-depth assessments of over 13 representative SPEs, supported by interviews with experts familiar with their implementation and operation. These examples were selected from a broader inventory of SPEs across Europe. 

The report concentrates on identifying typical models and recurring patterns, along with the associated technical and governance requirements. 

The report highlights that the fragmented policy landscape has resulted in a similarly fragmented architectural landscape, leading to the emergence of various SPE designs, each with distinct objectives, including: 

- Secure access to controlled data 

- Secure collaboration 

- Distributed computational approaches 

- Data lakes 

Among the 13 infrastructures examined in detail, most focus on enabling secure collaboration, while a few focus on secure access to controlled data, and one each provides “compute-to-data” capabilities and data lake functions. 

HealthyCloud deliverable D7.4<sup>41</sup> , on the other hand, gathered information on security policies and breach response protocols related to the same infrastructures examined in D5.1. This report presents an overview of current practices related to identification of users and access control, data processing, managing and monitoring the environment, as well as organisational policies and procedures. Given that these environments are built and operated in various ways, they each have distinct privacy requirements. Nevertheless, there is a strong consensus on the establishment of SPEs. The key findings are summarised as follows: 

- Most infrastructures employ federated authentication and view multi-factor authentication (MFA) as crucial for effective identity and access management. 

- Each project should operate within a dedicated environment that is technically and logically isolated from others, grouped by project rather than user. 

- Infrastructures managing permits automatically lock user environments once data permits expire and regularly verify the validity of access. 

41 HealthyCloud deliverable D7.4 https://zenodo.org/records/10225422 

117 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



- For health data processing, pseudonymised data with minimised variables is used, transferred in encrypted form, and must be audited before leaving the infrastructure. 

- All infrastructures implement various technical and organisational measures for security management, guided by institutional policies for federated infrastructures. 

- Most respondents have internal and external policies for users and staff, with certified sites offering more comprehensive documentation and staff training as a common best practice. 

### **Global Alliance for Genomics and Health (GA4GH)** 

The Global Alliance for Genomics and Health (GA4GH)<sup>42</sup> develops open, interoperable standards to facilitate secure, ethical, and scalable genomic and health data sharing. These standards provide technical frameworks for authentication, encryption, access control, federated analysis and data governance, which are also key elements for SPEs. 

Among these, **Crypt4GH** is a secure encryption standard specifically designed for genomic data. It ensures data remains protected both at rest and in transit through multi-layer encryption, allowing authorised users to decrypt only the portions they are permitted to access. Another standard is **GA4GH Passports** , which streamline authentication and authorisation by providing a federated identity management system. This allows users to securely access SPEs using credentials from their home institutions while enforcing finegrained access controls. 

SPE providers benefit from a user-friendly, secure, interoperable, and privacy-preserving toolkit designed to support the management and processing of sensitive biomedical data. 

### **GDI and 1+MG** 

The _Genomic Data Infrastructure_ (GDI)<sup>43</sup> project is enabling access to genomic and related phenotypic and clinical data across Europe. It is doing this by establishing a federated, sustainable and secure infrastructure to access the data according to the 1+ Million Genomes Initiative<sup>44</sup> 

The GDI project places emphasis on federated processing of genomic data which – in case the data in question falls under EHDS – provides a strong driver to solve SPE interoperability and federation in a standardised manner. Additionally, the scale of compute and storage resources needed for genomic data will impact the high-end SPE requirements, for example, driving the high-performance and cloud compute systems used for GDI data to comply with EHDS SPE requirements. 

Access to categories of data in focus of the GDI project can be split in three tiers: _open, registered_ and _controlled_ . These permissions are designed to be machine readable (Ga4GH passports). 

> 42 GA4GH <u>https://www.ga4gh.org/</u> 

> 43 GDI <u>https://gdi.onemilliongenomes.eu/</u> 

> 44 1+ Million Genomes Initiative https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes 

118 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



The 1+MG Framework<sup>45</sup> is a series of components based on the output of the 1+MG projects that provide guidance on ELSI, data quality, data standards, and technical infrastructure standards and APIs. 

### **Sensitive Data HPC strategy (CSC, Finland)** 

SD HPC is the Sensitive Data High Performance Computing solution from CSC – IT Center for Science Ltd., Finland. It is based on the secure transfer of batch job requests from its Secure Processing Environment (SPE) SD Desktop. It contains a batch job management process not visible to other users, secure transfer of user data into a dedicated compute node when the job enters the execution, isolation of the compute node during the execution, and return encrypted results to the SPE user storage space. 

The SD HPC service is currently deployed in the CSC Puhti supercomputer. It is in alpha user testing phase. 

SD HPC receives job description files from users in the SD Desktop SPE project environment (Annex 8: Figure 3). The HPC system must recognise the user and their project. In writing the job description file, the user must consider the capabilities and limitations of the HPC. The dedicated sensitive data execution manager queues and launches the job in a dedicated node. It also copies user resources from SPE storage before isolating the node for the duration of the job execution. It returns the execution results to the user project environment and cleans any trace of the execution event from the node. 

**Annex 8: Figure 3.** CSC’s sensitive data HPC strategy view 



<!-- Start of picture text -->
SPE Ei} ‘SD HPC c:<br>Project environment (i)<br>Storage OD Data and information systems<br>Job wo Sensitive (i> Analysis (i> ‘Shared user GD<br>file identities<br>11,1 description data programme and project<br>Compute >CompetencesCompetences and2 human resources<br>Creationsubmissionof GI} | Understanding (| _—_Understanding(i) Hc<br>files ofrequirements data analysis capabilitiesof the HPC maintenance<br>Processes and models<br>Sensitive data GD) HPC node | —Node reset Gi}<br>job execution dedication and data<br>manager mechanism erasure<br>bidirectioinal<br>Secureinterfacequery> dataSecuretransfer Gp<br><!-- End of picture text -->

45 1+MG framework https://framework.onemilliongenomes.eu/ 

119 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



The job request message from the user is passed through the backend gateways to the main HPC gateway called SDSI server (Annex 8: Figure 4). The acronym comes from Sensitive Data Slurm Interface indicating the used batch job controller. The SDSI server has complete control of the job management once the job request has been submitted to the HPC system. This isolates the client side cleanly from the HPC execution.   Expansion of SD HPC to other HPC systems requires only the adaptation of the SDSI server to their specific capabilities and architecture that needs extensive involvement of their system maintainers. 

Inside the SD HPC service, the SDSI server formats the job submission to the requirements of the batch job controller (Annex 8: Figure 4). Once the job enters the execution, it fetches the header parts of the user input files from the internal vault component of SD Connect. Before dispatching the headers, the vault re-encrypts the headers with job-specific encryption key according to the SDSI server instructions. These headers are combined with the encrypted payload from SD Connect before passing them into the HPC compute node reserved for the job. The separation of headers and their separate encryption from the payload is an envelope encryption capability of the GA4GH Crypt4GH<sup>46</sup> file container format. 

Once all files have been copied to the job node, all access to the node is cut off. Communication to the node is resumed only after the execution is finished, decrypted input files have been removed, and the result files are encrypted with the project key. The SDSI server then copies all result files to a new folder in the SD Connect project space, removes all user files, resets the HPC compute node, and returns it to the pool. 

> 46 Global Alliance for Genomics and Health (GA4GH) Cryp4GH https://samtools.github.io/hts- <u>specs/crypt4gh.pdf</u> 

120 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



**Annex 8: Figure 4.** Service diagram showing the user initiating the SD HPC call. Solid arrows represent message directions and dashed lines file transfers. 



<!-- Start of picture text -->
‘SDS Frontend<br>SD Desktop =O SD Connect f=)<br>= oe os © SDS Vault ©<br>——><br>' i H ,<br>Terminal -O Front-end -Of j<br>proxy gateway H' H'<br>HH<br>HH<br>H H<br>| H H<br>job description file input files result files<br>SDS Backend | H H<br>Backend -O i H<br>gateway H H<br>HH<br>HH<br>HH<br>HH<br>Ht<br>AH<br>SD HPC ' i oO<br>SDSI server oO | '<br>job submissionI keys &headerst |' H'<br>+ | ¥ H<br>controllerBatch job ©|§ ————» Compute node f=)<br><!-- End of picture text -->

Using the language of the DARE UK Federated Architecture Blueprint<sup>47</sup> , the SD HPC is implemented as an indirect query. It also fulfils other requirements of data privacy and accountability for secure federated analysis: Identity, source and target of all transfers are known, validated, and accounted for, and all data and communication are encrypted in transit. The guaranteed ephemerality of personal data and isolation of processing within the HPC system makes SD HPC a special case of federated analysis with exceptionally strong data privacy guaranties. 

### **NORTRE, infrastructures for sensitive data in Norway** 

NORTRE<sup>48</sup> (Norwegian Trusted Research Environments) is a collaboration between the three main institutional research infrastructures for sensitive data in Norway, TSD<sup>49</sup> (services for sensitive data) at University of Oslo (UiO), HUNT Cloud<sup>50</sup> at the Norwegian University of 

> 47DARE UK Federated Architecture Blueprint https://zenodo.org/records/14192786) 

> 48 NORTRE https://nortre.no/ 

> 49 Tjenester for Sensitive Data (TSD) https://www.uio.no/tjenester/it/forskning/sensitiv/ 

> 50 HUNT Cloud https://about.hdc.ntnu.no/ 

121 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



Science and Technology (NTNU) and SAFE<sup>51</sup> (secure access to research data and e- infrastructure) at University of Bergen (UiB). The three partners share knowledge and expertise so scientists and data controllers from Norway and around the world can collect, analyse, store, share and collaborate on sensitive data in an optimised and trustworthy manner. 

In accordance with EHDS2, Norway has an ongoing project SPUHiN<sup>52</sup> which, among others, aims to prepare NORTRE for EHDS Regulation. This includes work such as drafting a requirements list, closely aligned with the requirements of the EHDS Regulation, which will be a goal for the three SPEs to achieve. SPUHiN is also creating a GAP analysis/list of points to be followed up with NORTRE to close these gaps. 

### **Secure data transfer solutions (Finland)** 

In Finland, CSC has developed Supertunneli (“Super Tunnel”)<sup>53</sup> , an advanced solution designed to address limitations in current data transfer services, particularly for large datasets. Based on the widely adopted S3 interface, Supertunneli significantly improves capacity compared to earlier systems, which were limited to a 4 GB maximum file size per transfer. This enhancement reduces manual workload and minimises the risk of errors typically associated with managing large datasets, particularly for projects utilising AI or machine learning. 

Supertunneli enables the secure transfer of large datasets in a single operation and initially supports transfers of at least 1 terabyte (1 TB). Transfers exceeding this threshold are also supported but require prior notification to Findata, Finland’s data permit authority. Additionally, the process can be optimised by automating data encryption and decryption. 

The connection used in the transfer of the files is encrypted and requires private/public keys exchange to allow the transfer. The transferred data is encrypted with Crypt4GH -encrytion tools provided by Global Alliance for Genomics and Health. 

In compliance with Finland’s Secondary Use Act, Supertunneli will serve as the standard interface for transferring datasets to approved secure processing environments. This ensures both regulatory alignment and improved security during data exchange. 

Further developments include leveraging the S3 interface to support the anonymisation and submission of research results. A complementary system, Tulostunneli (“Results Tunnel”), is under development and will enable secure environments to automate the delivery of published outputs directly to Findata. This replaces the current manual process, traditionally the responsibility of researchers, thereby enhancing security and ensuring consistent anonymisation of disseminated results. 

> 51 SAFE https://www.uib.no/safe 

> 52 SPUHiN https://www.helsedirektoratet.no/om-oss/forsoksordninger-og-prosjekter/fair-secureprovision-and-use-of-health-data-in-norway-spuhin 

> 53 Supertunneli https://findata.fi/en/news/supertunneli-launching-in-may-2025-as-part-of-transfer- <u>service-update/</u> 

122 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



For smaller or individual data transfers, the existing Tunneli service will remain in operation, providing a flexible, tiered approach to data exchange infrastructure in Finland. 

### **Anonymity verification tool (Finland)** 

In Finland, Findata is launching a new tool called Portti<sup>54</sup> in Kapseli to simplify and speed up the process of verifying the anonymity of research results. With this update, users no longer need to complete separate summary forms. 

Portti – Finnish for _Gateway_ – allows users to send results directly for anonymity verification. It enhances data security and streamlines the process for both users and Findata staff. 

Portti is strictly for transferring anonymous results. Personal data or non-anonymised information must not be submitted via the tool. To use Portti, users create a new transfer, upload the necessary files, fill in the required details, and select the result type. The results are then submitted to Findata for verification. 

Findata processes submissions as quickly as possible, and within a maximum of five working days. Once approved, results are automatically delivered to the user’s workspace, where they can be downloaded. Approved results remain available in the workspace for six months. 

If anonymity issues are found, Findata will send instructions for corrections via email and may request additional information if needed before final approval. 

The tool is being developed as part of the FinHITS project, co-funded by the European Union. 

### **Building a secure health data network (Norway)** 

In Norway, Norwegian Directorate of Health (NDH), National Institute of Public Health (FHI) and NORTRE<sup>55</sup> are working together in the SPUHiN<sup>56</sup> project to ensure that sensitive data transfers within Norwegian data holders, SPEs and Authorities (Coming HDABs) are secured and guaranteed. 

This will be done by building a HealthData@NO network based on the 4-corner model for the eDelivery model<sup>57</sup> . The 4-corner model ensures that data are encrypted, signed and addressed before leaving their safe environments. The 4 corner models addressing system, implemented by among other EU central Servies, guarantees that the data can only be delivered to an approved organisation registered at a central exchange register. 

The network aims also to be HealthData@EU compatible by following the eDelivery standard when there are cross border data transfers. 

> 54 Portti https://findata.fi/en/news/new-tool-for-kapseli-result-submission-will-launch-in-september/ 

> 55 <u>NORTRE</u> 

> 56 <u>FAIR Secure Provision and use of health data in Norway (SPUHiN) - Helsedirektoratet</u> 

> 57 <u>How does eDelivery work</u> 

123 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 9: Overview of relevant EU regulations** 

The EHDS will provide a trustworthy setting for secure access to and processing of a wide range of health data. It builds further on the General Data Protection Regulation (GDPR), Data Governance Act (DGA) and Network and Information Systems Directive (NIS2). 

These regulations collectively shape the landscape for SPEs, influencing their design, implementation, and operation in several critical ways. The following sections explore in greater detail how EHDS, GDPR and NIS2 shape the architecture and operational principles of SPEs, ensuring that they can securely and efficiently support the goals of the EHDS and GDPR. Notably, EHDS Article 73 serves as the primary reference for the general requirements of SPEs within the EHDS framework. 

### **EHDS article 73 analysis to deduce SPE requirements** 

The logic of creating EHDS-specific requirements is presented as architecture graphs with the source paragraph as the figure legend. 

**Annex 9: Figure 1. EHDS article 73(1).** Health data access bodies shall provide access to electronic health data pursuant to a data permit only through a secure processing environment which is subject to technical and organisational measures and security and interoperability requirements. In particular, the secure processing environment shall comply with the following security measures: 



<!-- Start of picture text -->
EHDS article 73(1) if)<br>Electronic ©<br>Health Data<br>(EHD)<br>provide access to) Data permit © ne<br>pisses Creates . ‘<br>Healt Data CD SPE O TOMS<br>Access Body ©————provide access through —comply with<br>(HDAB)<br>1<br>H<br>! EHDSR-1. HDAB MUST grant access to EHD 7<br>h-- 2) using a data permit<br>! EHDSR-2. EHD MUST be accessed using an (7<br>\-->} SPE<br><!-- End of picture text -->

124 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 9: Figure 2. EHDS article 73(1)(a)** . _The restriction of access to the secure processing environment to authorised natural persons listed in the data permit issued pursuant to Article 68;_ 



<!-- Start of picture text -->
EHDS article 73(1)(a) o<br>Data permit © Authorised CD SPE ©<br>solisted in health data —access restricted to—<br>user<br>1<br>i EHDSR-3. Natural persons listed in the data <7<br>‘==> permit MAY access the identified EHD in SPE<br><!-- End of picture text -->

**Annex 9: Figure 3. EHDS article 73(1)(b).** _The minimisation of the risk of the unauthorised reading, copying, modification or removal of electronic health data hosted in the secure processing environment through state-of-the-art technical and organisational measures;_ 



<!-- Start of picture text -->
EHDS article 73(1)(b) in}<br>Unauthorised CD SPE OO ToMs<br>user minimise risk— comply with—<br>T<br>H<br>' EHDSR-4. TOMs MUST minimise the risk of (7<br>S-- 3) unauthorised EHD access in SPEs<br><!-- End of picture text -->

125 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 9: Figure 4. EHDS article 73(1)(c).** _The limitation of the input of electronic health data and the inspection, modification or deletion of electronic health data hosted in the secure processing environment to a limited number of authorised identifiable individuals;_ 



<!-- Start of picture text -->
EHDS article 73(1)(c) oO<br>| Uniqueidentity user 77+— healthAuthoriseduser data CDlisted in-- Data permit ©<br>1<br>access restricted to<br>i<br>SPE (an)<br>i<br>H<br>{--> ~ permit EHDSR-3.MAY Naturalaccesspersonsthe identifilist ed inEHD theindataSPE7<br>1<br>' REHDS-S. Authorised health data users (7<br><=> MUST be strongly identified<br><!-- End of picture text -->

**Annex 9: Figure 5. EHDS article 73(1)(d).** _Ensuring that health data users have access only to the electronic health data covered by their data permit, by means of individual and unique user identities and confidential access modes only;_ 



<!-- Start of picture text -->
EHDS article 73(1)(d) (A)<br>| ~ Uniqueidentity user 7WH Authorisedhealthuser data CDlisted in -- Data permit 3<br>1<br>access restricted to<br>1<br>| accessConfidential mode <7/H— SPE (an)<br>$$<br>!<br>| EHDSR-S. Authorised health data users 7<br>> MUST be strongly identified<br><!-- End of picture text -->

**Annex 9: Figure 6. EHDS article 73(1)(e).** _The keeping of identifiable logs of access to and activities in the secure processing environment for the period necessary to verify and_ 

126 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



_audit all processing operations in that environment; logs of access shall be kept for at least one year;_ 



<!-- Start of picture text -->
EHDS article 73(1)(e) oO<br>Identifiable &<br>access log SPE fon)<br>verify and audit (7 All processing<br>all processing — operations<br>operations logs<br>$$<br>1<br>H<br>EHDSR-6. All access and operation logs of (7<br>heH -+ ‘SPE MUST be availableauditing for verification and<br>1<br>'<br>bee1 ~ EHDSR~7. All SPE logsactor MUST identify the 7<br>i —<br>H EHDSR-8. All SPE logs MUST be kept at least 7<br>Se= + for one year<br><!-- End of picture text -->

**Annex 9: Figure 7. EHDS article 73(1)(f).** _Ensuring compliance and monitoring the security measures referred to in this paragraph to mitigate potential security threats._ 



<!-- Start of picture text -->
EHDS article 73(1)(f) it}<br>| Mitigatesecurity threatspotential (7— SPE O<br>!<br>' EHDSR-9. TOMs of SPEs MUST be monitored (7<br>San for security<br><!-- End of picture text -->

**<mark>Annex 9: Figure 8. EHDS article 73(2).</mark>** _<mark>Health data access bodies shall ensure that electronic health data from health data holders in the format specified in the data permit can be uploaded by those health data holders and can be accessed by the health data user in a secure processing environment.</mark>_ 

_<mark>Health data access bodies shall review the electronic health data included in a download request to ensure that health data users are only able to download non-personal electronic health data, including electronic health data in an anonymised statistical format, from the secure processing environment.</mark>_ 

127 



D7.4 Technical, functional and security specifications of Secure Processing Environments 



<!-- Start of picture text -->
EHDS article 73(2) oO<br>Health data CO)<br>holder<br>Healt Data CD Upload SPE O)<br>(HDAB)<br>create i<br>8 ¥<br>Data permit Electronic &<br>(EHD)<br>‘listed in<br>“a<br>Authorised CD<br>health data —_-access restricted to-<br>user<br>ture$a<br>gen Download Ah sersterstsrsesseeseenee)<br>only<br>¥<br>non-personal 5<br>electronic<br>health data<br>H<br>1<br>H EHDSR-10. EHD MUST be identified in the 7<br>oe data permit<br>‘<br>‘[s--> EHDSR-11.the permittedHealthEHDdata holderto be available MUSTin uploadan SPE -7<br>! for the health data user<br>Hl' a<br>H EHDSR-12. Health data user MAY download 7<br>h---» only non-personal EHD from SPE.<br>i Anonymised personal data is non-personal<br>'5<br>'7<br>' EHDSR-13. HDAB SHALL ensure by reviewing<br>==> that no personal data is taken out of the SPE<br>by the health data user<br><!-- End of picture text -->

**Annex 9: Figure 9. EHDS article 73(3).** _Health data access bodies shall ensure that audits of the secure processing environments are carried out on a regular basis, including by third_ 

128 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

_parties, and shall take corrective action for any shortcomings, risks or vulnerabilities identified by those audits in the secure processing environments._ 



<!-- Start of picture text -->
( EHDS article 73(3) oO<br>Healt Data CD SPE OO) Regular audits and <><br>‘Access Body<br>‘on demand<br>(HDAB)  —provide access through— — corrective measures<br>———————— eee<br>HH a<br>f--> securityEHDSR-14.auditsRegularMUST internalbe done andon externalSPE TOMs (7<br>H<br>Hfh-o EHDSR-15. SPE TOMs MUST undergo risk (><br>H assessments<br>i EHDSR-16. HDABs MUST ensure that SPE 77<br>‘1 TOMs audits are carried out and that risk<br>assessments lead to risk mitigations<br><!-- End of picture text -->

**Annex 9: Figure 10. EHDS article 73(4).** _Where recognised data altruism organisations under Chapter IV of Regulation (EU) 2022/868 process personal electronic health data using a secure processing environment, those environments shall also comply with the security measures set out in paragraph 1, points (a) to (f), of this Article._ 



<!-- Start of picture text -->
EHDS article 73(4) (03)<br>2023/2854 K]eveeees organisation =@—————_»<br>| Data Act EU (1) Data altruism CD SPE oO<br>H<br>1<br>H‘- -*| EHDSR-17.Data Actrequirements areWhen used forSPEsMUST EHD,mentionedbe EHDSfollowed rulesin the andEU 7<br><!-- End of picture text -->

**Annex 9: Figure 11. EHDS article 73(5).** _By ... [two years from the date of entry into force of this Regulation], the Commission shall, by means of implementing acts, lay down the technical, organisational, information security, confidentiality, data protection and interoperability requirements for the secure processing environments, including with regard to the technical characteristics and tools available to the health data user within the secure_ 

129 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



_processing environments. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 98(2)._ 



<!-- Start of picture text -->
EHDS article 73(5) it}<br>SPE oO Implementing (7<br>| acts<br>|<br>comply with<br>|<br>TOMs oO<br>security<br>| Technical (7 Information (7 Data protections7<br>| Organisational (7 | Confidentiality -7 Interoperability <7<br>Ee<br>1<br>1' EHDSR-18. SPEs SHALL adapt to TOMs—that (7<br>Ls) the Commission will write into EHDS<br>implementing acts<br><!-- End of picture text -->

### **Key GDPR data and processing requirements** 

When developing technical specifications for SPEs, several GDPR articles must be considered to ensure compliance with data protection requirements. These articles include: 

**Article 5 – Principles relating to processing of personal data** : This article outlines the core principles of data processing, including data minimisation, purpose limitation, accuracy and storage limitation. SPEs must be designed to process only the necessary data for defined purposes and ensure data is accurate and not retained longer than necessary. (Annex 9: Figure 12) 

130 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

**Annex 9: Figure 12. GDPR Article 5** – Principles relating to processing of personal data 



<!-- Start of picture text -->
| GDPREU (1) GDPR Article 5 on personal data principles oO<br>2016/679 ~ GDPR Art. 5(1)(a) (A) GDPR Art. 5(1)(b) in) GDPR Art. 5(1)(e) if)<br>Data © | Lawfulness | | Purpose limitation | ; Storage limitation<br>controller [> GDPR Art. 5(1ya) GDPR Art. 5(1(@) GDPR Art. 51M (I)<br>+ | Fairness | | Minimisation | Integrity<br>PesceasenData = | GDPRTransparencyArt. 5(1(@) (1) | | GDPRAccuracyArt. (1d) (I) | GDPRA.Confidentiality51M)<br>Accountability<br>| GDPR Art. 5(2) in)<br><!-- End of picture text -->

**Article 25 – Data protection by design and by default** : This article requires incorporating data protection measures into the design of systems, ensuring that privacy is considered from the outset and that the SPE is configured to minimise data exposure by default (Annex 9: Figure 13). 

**Annex 9: Figure 13. GDPR Article 25** – Data protection by design and by default 



<!-- Start of picture text -->
GoPREU (]) GDPR Art. 25 Data protection by design and by default oO<br>2016/679  <>—<br>Transparency (1) lawfulness (1) Fairness (1) | limitationPurpose (1) minimisationData =)<br>Data<br>controller |----D} Accuracy (i) Storage (1) Integrity and (1) Accountability (1)<br>limitation confidentiality<br>f a 2.1.3 Elements to take into account<br>processor 2.1.3.1 “state (F) 2.1.3.2 “cost of (1) 2.1.3.3 “nature, (7) 2.1.3.4 “risks of varying (1)<br>of the art” implementation” scope, context likelihood and severity for<br>and purpose of rights and freedoms of<br>processing natural persons posed by the<br>processing”<br>2.1.4 Time aspect<br>2.1.4.1 At the time of the (J) 2.1.4.2 At the time of the (I)<br>determination of the means processing itself (maintenance<br>for processing and review of data protection<br>requirements)<br><!-- End of picture text -->

**Article 32 – Security of processing** : This article mandates that appropriate technical and organisational measures, such as encryption, access control, and regular security 

131 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

assessments, are implemented to ensure the security of personal data processed within SPEs (Annex 9: Figure 14). 

**Annex 9: Figure 14. GDPR Article 32** – Security of processing 



<!-- Start of picture text -->
2016/679<br>| (GDPR EU Oo GDPR Art. 32 Security of processing 113)<br>GDPR Art. 32(1) a)<br>Cee Ww GDPR Art. 32(2) Level of (1)<br>Data encryptionPseu ceof personalbeh 4data riskssecurityresulting takes into from account processing the |<br>coli le GDPR Art. 32(1)(b) Ensure (1)<br>trustworhinessthe ongoingof services | GDPR Art. 32(3) Demonstrate {1)<br>compliance to a code of<br>Data) GDPR Art. 32(1)(€) Fault (I) a aeea<br>processor tolerance to physical or |<br>technical incidents —<br>———————_ GDPR Art. 32(4) Operatonal oO<br>GDPR Art. 3204) measures to ensure natural<br>Continuouseffectiveness evaluationof TOMs of | persons adhere to instructions<br><!-- End of picture text -->

The Article 32 requires specific measures to protect sensitive health data and ensure that it is processed securely. 

Firstly, data protection by design and by default, as specified in Article 25, is essential. SPEs should isolate health data from other environments to prevent unauthorised access. By separating sensitive data, SPEs limit exposure to only those with verified access permissions. Additionally, role-based access control systems must be implemented to ensure that only authorised individuals, based on their specific roles and responsibilities, can access the data. This ensures that access is tightly controlled and compliant with GDPR's requirements for data security. 

In addition to isolation and access control, encryption is a cornerstone of the SPE security protocols, directly supporting Article 32(1)(a), which mandates appropriate security measures. All health data within the environment should be encrypted both in transit and at rest, to prevent unauthorised access and helping to protect data integrity and confidentiality. 

The integration of privacy-preserving technologies, such as anonymisation and pseudonymisation, aligns with Article 32(1)(a) and Article 25(1). These techniques reduce the risk of re-identification and protect data subjects’ privacy while enabling secure data processing. The guidelines for implementing these privacy-preserving technologies will be outlined as part of T7.2 in TEHDAS2. 

SPEs should also undergo regular security assessments and penetration testing to identify any vulnerabilities and maintain compliance with Article 32(1)(d), which requires ongoing evaluation of the effectiveness of security measures. Robust incident detection and response protocols must be in place to swiftly manage any potential data breaches. 

132 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



Finally, accountability and documentation are crucial to maintaining GDPR compliance. In accordance with Article 5(2), which emphasises the accountability principle, and Article 30, which requires detailed records of processing activities, SPEs should maintain comprehensive records of all security measures and access logs. Regular internal and external audits should be conducted to verify that the SPE is consistently meeting GDPR’s privacy and security standards. 

### **NIS2 Directive** 

The NIS2 Directive (Directive (EU) 2022/2555) is the EU’s key cybersecurity legislation, aimed at enhancing the cybersecurity posture across the Union by improving the resilience and incident response capacities of essential and important entities in critical sectors. 

The NIS2 Directive establishes stronger cybersecurity requirements for critical infrastructure across the EU, with the specific obligations defined through national transpositions. SPEs handling sensitive health data will generally fall within scope, requiring compliance with stringent security measures such as endpoint protection, intrusion detection systems, and incident response protocols. They must also demonstrate resilience against cyberattacks and operational risks, ensuring continuity of service and the secure handling of data. 

### **Role of CSIRTs under NIS2** 

Under the NIS2 Directive, each EU Member State is required to establish its own Computer Security Incident Response Team (CSIRT). These national CSIRTs act as the single point of contact for receiving notifications related to cybersecurity incidents, threats, and near misses within their respective countries. 

### **Cybersecurity risk-management measures under NIS2** 

According to NIS2, entities must implement cybersecurity risk-management measures based on an all-hazards approach, designed to protect both network and information systems and their physical environment from incidents. At a minimum, these measures must include: 

(a) policies on risk analysis and information system security 

(b) incident handling 

(c) business continuity, such as backup management and disaster recovery, and crisis management 

(d) supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers 

(e) security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure 

(f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures 

133 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

(g) basic cyber hygiene practices and cybersecurity training 

(h) policies and procedures regarding the use of cryptography and, where appropriate, encryption 

(i) human resources security, access control policies and asset management 

(j) the use of multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems within the entity, where appropriate 

134 

D7.4 Technical, functional and security specifications of Secure Processing Environments 



# **Annex 10: Classification of risks and threats against SPEs** 

The table below (Table 10.1) is sourced from the French Digital Health Agency and is part of a report designed to help healthcare facilities implement the Politique Générale de Sécurité des Systèmes d’Information de Santé<sup>58</sup> , the legislative framework governing IT security in the health sector. 

**Table 10.1.** An example classification of risks and threats against general cybersecurity threats. 

|Event|Threat scenarios|Reference|Level of<br>risk|
|---|---|---|---|
|Unavailability of functions (medical<br>application, connected device,<br>etc.) or information (personal<br>health data or personal data of a<br>user) that may lead to service<br>disruption, a negative impact on<br>the image among users and/or a|Malicious code (virus, Trojan horse);<br>Degradation or interruption of the network (local network,<br>WAN and Internet access, WiFi network);<br>Power supply failure; Failure of server room air<br>conditioning; Handling error by IT staff; Lack of<br>maintenance;|R-01|High|
|,<br>user risk|Application saturation;<br>Uncontrolled modification of software.|R-02|Medium|
||Damage to computer equipment (fire, water damage,<br>etc.);<br>Unavailability of personnel (pandemic, health crisis,<br>difficulties accessing buildings, etc.).|R-03|High|
|Alteration of functions (medical<br>application, connected device,<br>etc.) or information (for example,<br>personal health data or personal|Malicious code (virus, Trojan horse); Input or command<br>error by an IS user; Lack of maintenance; Equipment<br>failure.|R-04|High|
|<br>data of a user) that may lead to<br>service disruption, a negative<br>impact on the image among users,<br>and/or a patient risk.|Uncontrolled modification of software (software update or<br>configuration/parameter changes);<br>Misuse of software's intended purpose (abuse of system<br>or application rights, direct access to application data,<br>etc.).|R-05|Medium|
||Computer intrusion.|R-06|Medium|
|Alteration of evidence elements<br>generated and stored by the IS<br>(e.g., application logs, etc.) that<br>may increase the legal risk for the|Misuse of a software's intended purpose (abuse of<br>system or application rights, direct access to application<br>data, etc.).|R-07|Medium|
|<br>organisation in case of litigation.|Computer intrusion.|R-08|Medium|
|Access to personal health data or<br>personal data of a patient by an<br>thid thid t|Loss or uncontrolled removal of equipment (laptop,<br>removable storage media, etc.).|R-09|High|
|unauorse r pary,<br>constituting a violation of privacy<br>and/or professional secrecy.|Misuse of a software's intended purpose (abuse of<br>system or application rights, direct access to software<br>data).|R-10|Medium|



58 PGSSI-S https://esante.gouv.fr/sites/default/files/media_entity/documents/pgssis_guide_pssi_non-expert-ssi-v-1.0.pdf 

135 



D7.4 Technical, functional and security specifications of Secure Processing Environments 

|Computer intrusion.|R-11<br>Medium|
|---|---|



PerMedCoE<sup>59</sup> , the HPC/Exascale Centre of Excellence for Personalised Medicine in Europe project, published a report<sup>60</sup> 2022 on about guidelines for HPC systems on cybersecurity. The architecture graph of their main findings is in Annex 10: Figure 1. 

**Annex 10: Figure 1.** Personalised medicine applications HPC security breach risks and impacts. 



<!-- Start of picture text -->
Negativeeffect Identification © Gainof © Decision- © Error ©<br>ofan statistical making recovery<br>individual information errors overhead<br>% ha % % %<br>1 7x i 1 i<br>Risk 1 oN 1 L L<br>Accidental @F Data theft @ Loss of @ Loss of @&<br>exposure by an integrity availability<br>of data adversary<br>4 4a 4 4<br>Common threat sources i i i<br>Threat actors Oo Ecosystem failure oO<br>vulnerable to Authorised (1) Unauthorised [1] Software [1] Hardware [1]<br>unintentional errors’ —_ users users failure failure<br>and mistakes<br>may act maliciously HPCstaffadmin 8) Externalactors 8)<br>to deliberately /—<br>impact the data<br>security<br>Threats specific to biomedical research<br>Data size [1] Reidentification (1) Clinical data (1) Data maximation [I]<br>based on internal exposes ways reguirements limit the<br>markers to harm application of<br>individuals minimality principle<br><!-- End of picture text -->

> 59 PerMedCoE https://permedcoe.eu/ 

> 60 D5.3 Derivation of general guidelines on data protection and privacy preservation of a use-case independent method/software development that will be exascale ready (September 2022) <u>https://permedcoe.eu/wp-content/uploads/2024/10/PMC-D5.3.pdf</u> 

