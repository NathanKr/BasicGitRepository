using Logic;
using Mocks;
using ProgressForms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Prod;

namespace ClassLibrary2
{
    public class ProgressFactory
    {
        // --- View know about Presenter 
        public static ProgressView CretaeView()
        {
            return new ProgressForm();
        }

        // Model know nothing about Presenter or View
        public static ProgressModel CreateModel()
       {
           ProgressModel oProgressModel = null;

           if (Constants.bModelMock)
           {
               oProgressModel = new ProgressModelMock();
           }
           else
           {
               oProgressModel = new ProgressModelImpl();
           }

           return oProgressModel;
       }

       // --- called inside view
       // --- Presenter knows about Model and View
       public static ProgressPresnter CreatePresenter(
           ProgressView oProgressView,
           ProgressModel oProgressModel)
       {
           return new ProgressPresnterImpl(oProgressView, oProgressModel);
       }
    }
}
