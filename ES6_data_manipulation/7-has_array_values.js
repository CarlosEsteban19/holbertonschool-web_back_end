export default function hasValuesFromArray(set, array) {
  if (array.every in set) {
    return true;
  }
  return false;
}
