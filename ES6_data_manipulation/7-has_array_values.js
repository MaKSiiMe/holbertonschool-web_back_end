export default function setFromArray(set, array) {
  return array.every((values) => set.has(values));
}