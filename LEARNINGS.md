
# LEARNINGS

## Día 1: tests, KeyError y dict.get

¿Para qué sirve un entorno virtual? ¿Qué problema evita?, ¿Qué hace uv frente a pip + venv?

Basicamente es un espacio aislado en tu computadora para cada uno de tus proyectos de programación, lo que causa es que en este ambiente tiene su propia copia o versión de python con sus propias librerias y caracteristicas. 

Ahora bien con venv, necesitas correr pip para poder instalar paquetes en ese entorno virtual, pero con uv esto pasa de ser un proceso largo a un proceos de segundos obteniendo el mismo resultado. 

### 1. KeyError = leí una llave que todavía no existe
- **Qué pasó:** `totals[uid] += x` falla con un usuario nuevo, porque `+=` primero lee y no hay nada que leer.
- **Por qué importa para AI Engineering:** los datos reales vienen incompletos (JSON de APIs, filas de Snowflake, respuestas de un LLM sin el campo esperado). Un pipeline que asume que los campos siempre existen se rompe en producción. Hay que tratar toda entrada como poco confiable.

### 2. Un bug silencioso es peor que uno que revienta
- **Qué pasó:** mi primera "corrección" no falló, pero daba totales incorrectos.
- **Por qué importa:** los sistemas de IA casi nunca revientan; responden algo plausible pero equivocado. Un modelo de churn con data leakage da un AUC excelente y está mal. Un agente puede devolver SQL que corre pero responde otra pregunta. Lo único que lo detecta es comparar contra un valor correcto conocido.

### 3. Un test = preparar, ejecutar, verificar contra un valor calculado a mano
- **Qué pasó:** definí la respuesta esperada antes de correr, y comprobé que el test pueda fallar.
- **Por qué importa:** es la estructura exacta de un eval: input, ejecutar el sistema, comparar con una respuesta esperada (golden set). Los tests son evals determinísticos; los evals de LLMs son lo mismo con un criterio más difuso. Un eval que no puede fallar no mide nada.

### 4. Cuando un test falla, primero decido: ¿falla la función o mi expectativa?
- **Qué pasó:** en la lista vacía esperaba `["No data"]`, pero lo razonable era `[]`. Una función debe devolver siempre el mismo tipo de dato.
- **Por qué importa:** en evals, a veces el error está en el golden set, no en el modelo. Y al diseñar herramientas para agentes, una tool que a veces devuelve lista y a veces texto confunde al agente. Definir el contrato de salida es diseño, no detalle.

### Bonus: regresión
- Cambié algo y el primer test, que ya pasaba, volvió a fallar. Para eso existen los tests. Con prompts y modelos pasa igual: cualquier cambio puede empeorar algo que funcionaba, y solo lo sabes si tienes evals que corran de nuevo.

### Que aprendí hoy 

- Apredí a crear, configurar y trabajar en ambientes de desarrollo, validar que algo funciona con comprobación. Un test es un eval en miniatura. Con agentes de código, tu trabajo es verificar. Vas a usar Claude Code desde la fase 2. Generar código se vuelve barato, y lo escaso pasa a ser saber si ese código es correcto. Sin tests, estás aceptando código que no puedes evaluar. Con tests, delegas con control.