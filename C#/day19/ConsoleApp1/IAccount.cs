public interface IAccount
{
    DateTime TransactionDate { get; }
    int Cr { get; set; }
    int Dr { get; set; }
    string Particulars { get; set; }

    string GetAccountInfo(); // Change return type to string
}
