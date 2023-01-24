def test(driver):
    script = """
    let a = document.getElementsByClassName("cat-button normal primary btn-send")[0]
    let resultado = a.getAttribute('disabled')

    return resultado
    """

    resultado = driver.execute_script(script)
    return resultado
