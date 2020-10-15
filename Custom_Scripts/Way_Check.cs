using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class Way_Check : UnitySubscriber<MessageTypes.Testing.array>
    {


        public static int[] way_result;

        
       
        protected override void Start()
        {
            base.Start();
            //way_result = new int[] { 3, 3, 3, 3, 3, 3 };
        }
        protected override void ReceiveMessage(MessageTypes.Testing.array message)
        {
            way_result = message.int_array;
        }
    }
}