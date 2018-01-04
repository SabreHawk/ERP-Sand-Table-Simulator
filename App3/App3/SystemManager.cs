using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using Windows.ApplicationModel;
using Windows.ApplicationModel.Activation;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Navigation;
using Windows.Networking.Sockets;


namespace App3
{
    class SystemManager
    {
        //服务器连接设置
        //设定服务器IP地址  
        //配置服务器IP与端口


        public static string UploadAndDownload(string Uploadstring)
        {
            IPAddress ip = IPAddress.Parse("45.77.112.171");
            Socket clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            clientSocket.Connect(new IPEndPoint(ip, 1830));
            clientSocket.Send(Encoding.UTF8.GetBytes(Uploadstring));

            byte[] result = new byte[1024];
            int receiveLength = clientSocket.Receive(result);
            clientSocket.Shutdown(SocketShutdown.Both);
            return Encoding.UTF8.GetString(result, 0, receiveLength);

        }


        ///////这个函数仅展示后台可以处理哪些功能d=====(￣▽￣*)b
        public static void function()///////这个函数仅展示
        {
            /*
            'sys_add_raw_material_info' 
            'sys_add_raw_material_order'
            'sys_update_raw_material_repository' 
            'sys_update_production_repository' 
            'sys_query_raw_material_info' 
            'sys_query_raw_material_order'
            'sys_query_raw_material_repository' 
            'sys_query_production_info' 
            'sys_query_production_repository'
            'sys_query_production_order' 
            'sys_get_raw_material_category_total_num'
            'sys_get_raw_material_category_remain_num'
            'sys_produce'这个是生产
            'sys_commit_production_order'
            'sys_login'这个是登陆
            */

        }

    }

}
