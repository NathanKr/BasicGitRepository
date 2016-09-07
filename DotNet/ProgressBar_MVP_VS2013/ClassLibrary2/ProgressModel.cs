using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary2
{
    public interface ProgressModel
    {
        // --- run inside progress

        // TBD out value to show progress details
        bool Run();
    }
}
