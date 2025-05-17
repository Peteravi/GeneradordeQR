import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_code(
    url: str,
    output_file: str = "qr.png",
    version: int = 1,
    box_size: int = 25,
    border: int = 5,
    fill_color: str = "black",
    back_color: str = "white",
    error_correction: int = ERROR_CORRECT_H
):
    try:
        # Configurar el código QR
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        
        # Añadir datos
        qr.add_data(url)
        qr.make(fit=True)
        
        # Crear imagen
        img = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )
        
        # Guardar imagen
        img.save(output_file)
        print(f"Código QR generado exitosamente en '{output_file}'")
        
    except Exception as e:
        print(f"Error al generar el código QR: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    generate_qr_code(
        url="https://peteravi.github.io/",
        output_file="qr_github.png",
        fill_color="#24292e",  # Color azul oscuro de GitHub
        back_color="#f6f8fa"   # Color gris claro de GitHub
    )