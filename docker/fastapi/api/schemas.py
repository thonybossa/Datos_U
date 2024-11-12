class MedicationData(BaseModel):
    expediente_invima: int = 123456
    principio_activo: str = "Paracetamol"
    concentracion: str = "500mg"
    unidad_base: str = "tableta"
    unidad_de_dispensacion: str = "blíster"
    nombre_comercial: str = "Acetaminofén Genérico"
    fabricante: str = "Laboratorios XYZ"
    medicamento: str = "Analgesico"
    canal: str = "Farmacia"
    precio_por_tableta: float = 0.50
    factoresprecio: str = "medio"
    numerofactor: int = 20