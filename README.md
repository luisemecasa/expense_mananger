# Expense_Mananger

Gestor de gastos 

## Integrantes del Grupo

- Luis Miguel Cañon 
- Johan Steven Polo

## Endpoints

A continuación se enumeran los endpoints utilizados en la API:

- **/income**
  - Método: POST
  - Descripción: Agrega una transacción de ingreso.
  - Tags: `income`
- **/income**
  - Método: GET
  - Descripción: Obtiene todas las transacciones de ingreso.
  - Tags: `income`
- **/income/{transaction_id}**
  - Método: DELETE
  - Descripción: Elimina una transacción de ingreso por su ID.
  - Tags: `income`
- **/expenses**
  - Método: POST
  - Descripción: Agrega una transacción de gasto.
  - Tags: `expenses`
- **/expenses**
  - Método: GET
  - Descripción: Obtiene todas las transacciones de gasto.
  - Tags: `expenses`
- **/expenses/{transaction_id}**
  - Método: DELETE
  - Descripción: Elimina una transacción de gasto por su ID.
  - Tags: `expenses`
- **/report/basic**
  - Método: GET
  - Descripción: Genera un informe básico de ingresos, gastos y saldo.
  - Tags: `report`
- **/report/expanded**
  - Método: GET
  - Descripción: Genera un informe detallado de ingresos y gastos por categoría.
  - Tags: `report`
