class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imag}i"
    
    def __eq__(self, __value: object) -> bool:
        return self.real == __value.real and self.imag == __value.imag