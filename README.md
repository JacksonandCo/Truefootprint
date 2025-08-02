# Truefootprint

This project aims to build a web application that estimates the end-to-end carbon footprint of a consumer product from production through transportation, usage and end-of-life disposal.

## Overview

Companies often provide only high-level carbon estimates, making it difficult for consumers to understand the true impact of their purchases. Truefootprint models the journey of a product using user-provided information (product name, weight, and shipment details) and calculates an approximate carbon footprint based on distance travelled, transport mode and emission factors. Manufacturing and disposal emissions are estimated using publicly available life-cycle assessment data.

## Features

- User input form for product details and tracking information.
- Calculation engine that multiplies distance by weight and transport-mode emission factors.
- Support for multiple transport legs (e.g., truck, ship, air).
- Integration of average manufacturing and end-of-life emission factors.
- Presentation of results with clear explanations.
- Repository includes emission-factor dataset and code for the calculation engine.
