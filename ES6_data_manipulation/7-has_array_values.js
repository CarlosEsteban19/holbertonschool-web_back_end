export default function hasValuesFromArray(set, array) {
  return array.every((index) => set.has(index));
}
