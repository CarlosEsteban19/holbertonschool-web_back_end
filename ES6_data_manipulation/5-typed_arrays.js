export default function createInt8TypedArray(lenght, position, value) {
  if (lenght <= position || position < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(lenght);
  const array = new DataView(buffer);

  array.setInt8(position, value);
  return array;
}
