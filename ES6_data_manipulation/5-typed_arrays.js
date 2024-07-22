export default function createInt8TypedArray(lenght, position, value) {
    if (lenght <= position || position < 0) {
      throw new Error('Position outside range');
    }
  const buffer = new ArrayBuffer(lenght);
  const array = new Int8Array(buffer);

  array[position] = value;
  return buffer;
}
