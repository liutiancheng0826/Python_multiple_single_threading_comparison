# Python_multiple_single_threading_comparison
This project described why sometimes using multiple threading is however slower than single threading.

Reasons:
在python中使用多线程反而慢
在Python中使用多线程反而慢的情况通常发生在I/O密集型任务中,
因为Python的全局解释器锁(GIL)限制了线程的并行执行。当线程在执行I/O操作时,
GIL会被释放,从而允许其他线程执行。但是,当线程在执行计算密集型操作时,
GIL不会被释放,导致线程无法并行执行。
