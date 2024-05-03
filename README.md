# Multi-Class-Prediction-of-Obesity-Risk


#### This project is an extension of improving the models previously developed for Kaggle Competition where we placed within the top 5%. The project aims at redoing the project with added production using best practices learned from class MGSC-695-076

### Meet the Team 
1. Product Manager - Aasna
2. Machine Learning Engineer - Arham
3. ML Ops - Krishan
4. Data Engineer - Yash
5. Cloud SME - Nandani
6. Business Analyst - Mahrukh

## Branches: 
1. Main: For Final Product [Owner - Team]
2. Experiments: For ML Experiments and tracking [Owners - Arham, Krishan]
3. ArchDevelopment: For CICD  [Owner - Nandani]
4. Streamlit: For front end [Owner - Nandani]
5. Data Engineering: For Kafka Streaming [Owner- Yash]
6. Backup: For Backup [Owner - Aasna, Mahrukh]

   
### Project Phases

#### Phase 1: Planning and Design 
During this initial phase, the team establishes the foundation of the project. The Product Manager sets the project's vision and milestones, while the Machine Learning Engineer and Business Analyst research technical feasibility and market requirements, respectively. The Data Engineer and Cloud SME lay the groundwork for data handling and cloud infrastructure, ensuring all systems align with the project’s technical needs. Access [planning and design documentation](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/11-Product-Manager).

#### Phase 2: Data Preparation and Infrastructure Setup 
In this phase, the team focuses on setting up the necessary infrastructure and preparing the data for analysis. The Data Engineer builds data ingestion pipelines, while the Cloud SME ensures the cloud setup is optimized for scalability and security.  Review the [infrastructure setup](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/05-Cloud-Architecture).

#### Phase 3: Feature Engineering and Model Prototyping 
Feature engineering and initial model prototyping are conducted. The Machine Learning Engineer explores and selects features that will effectively predict obesity risk, while developing initial models to test their efficacy. Access [feature engineering and prototyping details](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/03-Experiments).

#### Phase 4: Model Refinement and Experimentation 
This phase is critical for refining the models through extensive experimentation and tuning. The team iterates on models, optimizing their performance through advanced analytical techniques and continuous testing. Explore [model refinement experiments](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/03-Experiments).

#### Phase 5: Deployment Preparation and Testing
Preparation for deployment involves finalizing the model, setting up continuous integration/continuous deployment (CI/CD) pipelines, and ensuring all systems are robust and secure. The team conducts final stress tests to ensure the infrastructure is ready for a smooth transition to production. Details can be found in the [Docker](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/11-Docker) folder.

#### Phase 6: Model Deployment and Monitoring 
The model is deployed to a production environment. This phase includes rigorous monitoring of the model’s performance and quick resolution of any issues. The team focuses on ensuring the model operates efficiently and effectively. Monitor [deployment and operations](https://github.com/McGill-MMA-EnterpriseAnalytics/Multi-Class-Prediction-of-Obesity-Risk/tree/main/Streamlit).

### Technologies Used

- **Data Analysis/Model Training:** Python, Jupyter Notebooks
- **Experiment Tracking:** MLFlow
- **Model Building:** PyCaret, LightGBM, XGBoost, CatBoost
- **Hyperparameter Optimization:** Optuna
- **Containerization:** Docker
- **Realtime Data Streaming:** Kafka
- **Version Control and CI/CD:** Git, GitHub Actions
- **Cloud Deployment:** Azure Machine Learning, Azure Blob Storage
- **User Interface:** Streamlit
- **Dependency and Environment Management:** Poetry

### Business Case

Our solution targets healthcare providers for early identification of at-risk patients, public health officials for data-driven policy making, and insurance companies for premium adjustment based on individual risk. The economic impact includes significant healthcare cost savings and revenue generation from tailored wellness programs.

### Acknowledgements

This project is an effort by the team to tackle the global health crisis of obesity by employing advanced data science and machine learning techniques, aiming to make a significant impact in the healthcare sector.