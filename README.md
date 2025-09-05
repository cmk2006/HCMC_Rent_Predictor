# HCMC Rent Predictor
A machine learning application that predicts rental prices for apartments in **Ho Chi Minh City** using **linear regression**.  
It features a user-friendly GUI built with CustomTkinter and analyzes various factors including location, amenities, and property characteristics.

---

## 🏠 What is the HCMC Rent Predictor?
The **HCMC Rent Predictor** is a machine learning-powered tool for estimating apartment rental prices in Ho Chi Minh City.  
It uses **polynomial linear regression** to analyze:
- **Property characteristics** – floor area, bedrooms, bathrooms  
- **Location factors** – distance from city center  
- **Amenities** – washing machine, hot water, AC, parking, security  
- **Furnishing level** – unfurnished, basic, or fully furnished  

The application uses three main components:
1. **Machine Learning Model** – trained on real HCMC rental data using scikit-learn.  
2. **GUI Interface** – modern CustomTkinter interface for easy input.  
3. **Price Prediction** – instant rental price estimates in Vietnamese Dong.  

---

## 🛠️ Features
- Predicts rental prices using trained ML model.  
- Handles multiple property characteristics and amenities.  
- Interactive GUI with **Vietnamese language support**.  
- Real-time predictions with **formatted currency display**.  
- **Model persistence** – saves and loads trained models.  

---

## 📦 Installation
Clone the repository:
```bash
git clone https://github.com/cmk2006/HCMC_Rent_Predictor.git
cd HCMC_Rent_Predictor
```

Install required dependencies:
```bash
pip install pandas numpy scikit-learn customtkinter joblib
```

---

## 🚀 Usage

### Running the GUI Application
Launch the main application:
```bash
python GUI.py
```

### Using the Model Programmatically
```python
from call_linear_function import LinearRegression

# Example prediction
area = 60  # m²
bedrooms = 2
bathrooms = 1
washing_machine = 1  # 1 = Yes, 0 = No
distance_center = 5.0  # km
hot_water = 1
air_conditioning = 0
parking = 1
security = 1
furnishing = 1  # 0 = None, 1 = Basic, 2 = Full

predicted_price = LinearRegression.predict(
    area, bedrooms, bathrooms, washing_machine, 
    distance_center, hot_water, air_conditioning, 
    parking, security, furnishing
)

print(f"Predicted rental price: {predicted_price:,} VND")
```

---

## 📊 Dataset
The model is trained on **`Housing_data_final.csv`** containing Ho Chi Minh City rental data:

| Feature | Description | Values |
|---------|-------------|---------|
| `price` | Rental price in Vietnamese Dong | Continuous |
| `area` | Floor area in square meters | 17-177 m² |
| `bedrooms` | Number of bedrooms | 1-3 |
| `bathrooms` | Number of bathrooms | 0-3 |
| `washingmachine` | Washing machine availability | 0/1 |
| `dtcenter` | Distance from city center (km) | 0.3-21.4 km |
| `hotwater` | Hot water availability | 0/1 |
| `ac` | Air conditioning availability | 0/1 |
| `parking` | Parking availability | 0/1 |
| `security` | Security service availability | 0/1 |

---

## 🏗️ Project Structure
```
HCMC_Rent_Predictor/
├── GUI.py                    # Main GUI application
├── call_linear_function.py   # Model interface wrapper
├── linear_regression.py      # Core ML model functions
├── Housing_data_final.csv    # Training dataset
├── trained_model.pkl         # Saved trained model
├── trained_model_poly.pkl    # Saved polynomial features
├── README.md                 # Project documentation
└── LICENSE                   # MIT License
```

---

## 🔧 Technical Details

### Model Architecture
- **Algorithm**: Polynomial Linear Regression (degree=1)
- **Features**: 9 input variables
- **Framework**: scikit-learn
- **Serialization**: joblib for model persistence

### GUI Framework
- **Library**: CustomTkinter
- **Theme**: Light mode with blue color scheme
- **Language**: Vietnamese interface labels
- **Layout**: Grid-based responsive design

---

## 🚧 Known Issues
- **Syntax Error**: Extra 's' character in `GUI.py` line 105 needs removal
- **Market Limitations**: Predictions based on historical data only
- **Geographic Scope**: Limited to Ho Chi Minh City market

---

## 🤝 Contributing
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 🛣️ Roadmap
- [ ] **Web Interface** – Deploy as web application
- [ ] **Additional Cities** – Extend to other Vietnamese cities  
- [ ] **More Features** – Add distance to schools, hospitals, metro
- [ ] **Model Improvements** – Implement cross-validation and metrics
- [ ] **API Development** – REST API for external integration
- [ ] **Data Visualization** – Charts and graphs for market insights

---

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments
- **Data Source**: Ho Chi Minh City rental market data
- **GUI Framework**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **ML Framework**: [scikit-learn](https://scikit-learn.org/)
- **Inspiration**: Making rental price prediction accessible to everyone

---

## 📞 Contact
- **GitHub**: [@cmk2006](https://github.com/cmk2006)  
- **Project**: [HCMC_Rent_Predictor](https://github.com/cmk2006/HCMC_Rent_Predictor)

---

⭐ **Star this repo** if it helped you predict rental prices in Ho Chi Minh City!
