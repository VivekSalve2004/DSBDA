object BubbleSort {
  def bubbleSort(arr: Array[Int]): Array[Int] = {
    for (i <- arr.indices) {
      for (j <- 0 until arr.length - i - 1) {
        if (arr(j) > arr(j + 1)) {
          val temp = arr(j)
          arr(j) = arr(j + 1)
          arr(j + 1) = temp
        }
      }
    }
    arr
  }

  def main(args: Array[String]): Unit = {
    val arr = Array(5, 1, 4, 2, 8)
    println("Original Array: " + arr.mkString(", "))
    val sortedArr = bubbleSort(arr)
    println("Sorted Array: " + sortedArr.mkString(", "))
  }
}
