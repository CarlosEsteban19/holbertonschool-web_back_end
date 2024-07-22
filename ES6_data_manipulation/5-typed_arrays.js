export default function createInt8TypedArray(lenght, position, value) {
  const buffer = new ArrayBuffer(lenght);
  const array = Int8Array(buffer);

  if (lenght <= position || position < 0) {
    throw new Error('Position outside range');
  }
  array[position] = value;
  return buffer;
}
