import com.blue.python.syntax.module_a
com.blue.python.syntax.module_a.sayHello('Jason')

from com.blue.python.syntax.module_a import sayHello
sayHello('kevin')

from com.blue.python.syntax.module_a import sayBye as byebye
byebye('kevin')

from com.blue.python.syntax.module_a import *
sayGood('kevin')



print __name__