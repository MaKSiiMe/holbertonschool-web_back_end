export default function guardrail(mathFunction) {
  const queue = [(() => {
    try {
      return mathFunction();
    } catch (error) {
      return error.toString();
    }
  })(), 'Guardrail was processed'];
  return queue;
}
